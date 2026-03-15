"""
Action System - Combat, Reproduction, and Interactions
Handles all dot-to-dot and dot-to-world interactions

DOT AI 3.0: Added economic actions (Gather, Buy, Sell, Hold, Bribe)
"""

import random
import math


class Action:
    """Base class for actions"""
    
    def __init__(self, name, energy_cost):
        self.name = name
        self.energy_cost = energy_cost
    
    def can_execute(self, dot, world_state):
        """Check if action can be executed"""
        return dot.resources.energy >= self.energy_cost
    
    def execute(self, dot, world_state, delta_time):
        """Execute the action"""
        raise NotImplementedError


class AttackAction(Action):
    """Attack another dot"""
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.range = self.calculate_range()
        self.damage = self.calculate_damage()
        
        # Energy cost: 5% of max energy
        energy_cost = 0  # Will be calculated per dot
        super().__init__("attack", energy_cost)
    
    def calculate_range(self):
        """Attack range from DNA"""
        if not self.dna.attack.enabled:
            return 0
        
        base = 30  # pixels
        bonus = self.dna.attack.points * 2
        return base + bonus
    
    def calculate_damage(self):
        """Damage dealt from DNA"""
        if not self.dna.attack.enabled:
            return 0
        
        base = 10  # health points
        bonus = self.dna.attack.points * 0.5
        return base + bonus
    
    def can_execute(self, dot, world_state):
        """Can attack if gene enabled and energy available"""
        if not self.dna.attack.enabled:
            return False
        
        cost = dot.resources.max_energy * 0.05
        return dot.resources.energy >= cost
    
    def execute(self, dot, target_dot, delta_time):
        """Execute attack on target"""
        # 5% probabilistic failure
        if random.random() < 0.05:
            return {"result": "MISS", "damage": 0}
        
        # Calculate damage
        damage = self.damage
        
        # Apply defense reduction if target is defending
        # NOTE: Defending reduces damage but still loses health (just less)
        # Defender also pays 3% max_energy/second while defending
        if hasattr(target_dot, 'is_defending') and target_dot.is_defending:
            defense_reduction = 0.3 + (target_dot.dna.defend.points * 0.01)
            damage *= (1.0 - min(0.8, defense_reduction))
        
        # Apply damage
        target_dot.resources.deplete_health(damage)
        
        # Energy cost for attacker
        cost = dot.resources.max_energy * 0.05
        dot.resources.deplete_energy(cost)
        
        return {"result": "HIT", "damage": damage}


class DefendAction(Action):
    """Defensive stance - reduces incoming damage"""
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.reduction = self.calculate_reduction()
        super().__init__("defend", 0)  # Cost is per-second
    
    def calculate_reduction(self):
        """Damage reduction percentage"""
        if not self.dna.defend.enabled:
            return 0
        
        base = 0.3  # 30% base reduction
        bonus = self.dna.defend.points * 0.01
        return min(0.8, base + bonus)  # Cap at 80%
    
    def can_execute(self, dot, world_state):
        """Can defend if gene enabled and energy available"""
        if not self.dna.defend.enabled:
            return False
        
        cost = dot.resources.max_energy * 0.03
        return dot.resources.energy >= cost
    
    def execute(self, dot, world_state, delta_time):
        """Activate defensive stance"""
        # Energy cost: 3% per second
        cost = dot.resources.max_energy * 0.03 * delta_time
        dot.resources.deplete_energy(cost)
        
        dot.is_defending = True
        return {"result": "DEFENDING", "reduction": self.reduction}


class ReplicateAction(Action):
    """Reproduction - both sexual and asexual modes"""
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        super().__init__("replicate", 0)  # Cost varies by mode
    
    def can_execute_asexual(self, dot):
        """Can do asexual reproduction if energy > 80%"""
        if not self.dna.replicate.enabled:
            return False
        
        threshold = dot.resources.max_energy * 0.8
        return dot.resources.energy >= threshold and dot.resources.health > 70
    
    def can_execute_sexual(self, dot):
        """Can do sexual reproduction if energy > 40%"""
        if not self.dna.replicate.enabled:
            return False
        
        threshold = dot.resources.max_energy * 0.4
        return dot.resources.energy >= threshold and dot.resources.health > 70
    
    def can_execute(self, dot, world_state):
        """Can replicate (either mode) if gene enabled and minimum energy met"""
        return self.can_execute_sexual(dot) or self.can_execute_asexual(dot)
    
    def execute(self, dot, world_state, delta_time, mate=None):
        """Create offspring - sexual if mate provided, asexual otherwise"""
        from .dna import DNAProfile
        from .dot import Dot
        
        if mate is not None:
            # SEXUAL REPRODUCTION
            return self.execute_sexual(dot, mate, world_state)
        else:
            # ASEXUAL REPRODUCTION
            return self.execute_asexual(dot, world_state)
    
    def execute_sexual(self, parent_a, parent_b, world_state):
        """Sexual reproduction with DNA crossover"""
        from .dna import DNAProfile
        
        # Energy cost: 40% each parent
        cost_a = parent_a.resources.max_energy * 0.4
        cost_b = parent_b.resources.max_energy * 0.4
        
        parent_a.resources.deplete_energy(cost_a)
        parent_b.resources.deplete_energy(cost_b)
        
        # Health factor for offspring quality (0.8-1.0)
        health_factor_a = 0.8 + (parent_a.resources.health / parent_a.resources.max_health) * 0.2
        health_factor_b = 0.8 + (parent_b.resources.health / parent_b.resources.max_health) * 0.2
        avg_health_factor = (health_factor_a + health_factor_b) / 2.0
        
        # Create offspring DNA via crossover
        child_dna = DNAProfile.crossover(parent_a.dna, parent_b.dna)
        
        # Apply minor mutations (5% chance per gene, smaller changes)
        child_dna = self.mutate_dna(child_dna, mutation_rate=0.05, mutation_amount=2)
        
        # Spawn position (between parents)
        mid_x = (parent_a.position[0] + parent_b.position[0]) / 2.0
        mid_y = (parent_a.position[1] + parent_b.position[1]) / 2.0
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)
        child_pos = [mid_x + offset_x, mid_y + offset_y]
        
        # Clamp to world bounds
        bounds = world_state.get('bounds', {'width': 1200, 'height': 800})
        child_pos[0] = max(50, min(bounds['width'] - 50, child_pos[0]))
        child_pos[1] = max(50, min(bounds['height'] - 50, child_pos[1]))
        
        return {
            "result": "OFFSPRING_SEXUAL",
            "child_dna": child_dna,
            "child_pos": child_pos,
            "parent_a_id": parent_a.id,
            "parent_b_id": parent_b.id,
            "health_factor": avg_health_factor
        }
    
    def execute_asexual(self, dot, world_state):
        """Asexual reproduction (clone with mutations)"""
        from .dna import DNAProfile
        
        # Energy cost: 80%
        cost = dot.resources.max_energy * 0.8
        dot.resources.deplete_energy(cost)
        
        # Create mutated DNA
        child_dna = self.mutate_dna(dot.dna)
        
        # Spawn position (nearby parent)
        offset_x = random.randint(-30, 30)
        offset_y = random.randint(-30, 30)
        child_pos = [dot.position[0] + offset_x, dot.position[1] + offset_y]
        
        # Clamp to world bounds
        bounds = world_state.get('bounds', {'width': 1200, 'height': 800})
        child_pos[0] = max(50, min(bounds['width'] - 50, child_pos[0]))
        child_pos[1] = max(50, min(bounds['height'] - 50, child_pos[1]))
        
        return {
            "result": "OFFSPRING_ASEXUAL",
            "child_dna": child_dna,
            "child_pos": child_pos,
            "parent_id": dot.id
        }
    
    def mutate_dna(self, parent_dna, mutation_rate=0.1, mutation_amount=5):
        """Create mutated copy of parent DNA"""
        from .dna import DNAProfile
        
        # Clone parent DNA
        child_dna = parent_dna.clone()
        
        # Mutation parameters (configurable)
        
        for gene in child_dna.get_all_genes():
            # Skip eat gene (always enabled, no cost)
            if gene.name == "eat":
                continue
            
            # Mutate points
            if random.random() < mutation_rate:
                change = random.randint(-mutation_amount, mutation_amount)
                gene.points = max(0, min(50, gene.points + change))
            
            # Mutate enabled state (lower chance)
            if random.random() < 0.05:  # 5% chance to toggle
                gene.enabled = not gene.enabled
        
        # Ensure DNA is valid (doesn't exceed capacity)
        allocated = child_dna.get_allocated_points()
        if allocated > child_dna.total_points:
            # Reduce random genes until valid
            while child_dna.get_allocated_points() > child_dna.total_points:
                genes = [g for g in child_dna.get_all_genes() if g.points > 0 and g.name != "eat"]
                if genes:
                    gene = random.choice(genes)
                    gene.points = max(0, gene.points - 1)
        
        return child_dna


class BribeAction(Action):
    """
    DOT AI 3.0: Bribery/Negotiation System
    
    Allows dots to pay off aggressors to avoid combat.
    Two modes:
    1. Instant lump-sum bribe (traditional negotiation)
    2. Mercy mode activation (wallet trickle system)
    
    Research Question: Will attackers accept sub-lethal payment and retreat,
    or always escalate to murder for full wallet?
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        super().__init__("bribe", 0)  # No energy cost (just money)
    
    def can_execute(self, dot, world_state):
        """Can bribe if have money"""
        return dot.resources.wallet > 0
    
    def calculate_attack_expected_value(self, attacker, victim):
        """
        Calculate expected value of attacking victim to death.
        
        Used by attacker to decide: Accept bribe vs Continue attacking
        
        Formula:
        EV = P(kill) × Wallet_stolen - P(die) × Own_wallet_lost
        
        Returns: Expected monetary value of killing victim
        """
        # Probability of killing victim (based on relative strength)
        attacker_power = attacker.dna.attack.points if attacker.dna.attack.enabled else 1
        victim_defense = victim.dna.defend.points if victim.dna.defend.enabled else 1
        victim_health = victim.resources.health
        
        # Simple model: Higher attack vs lower defense+health = higher kill probability
        # Base 50% chance, modified by power differential
        power_differential = attacker_power - (victim_defense + victim_health / 20)
        kill_probability = 0.5 + (power_differential * 0.05)  # +/-5% per point difference
        kill_probability = max(0.1, min(0.95, kill_probability))  # Clamp to 10-95%
        
        # Probability attacker dies (counterattack risk)
        victim_power = victim.dna.attack.points if victim.dna.attack.enabled else 1
        attacker_health = attacker.resources.health
        death_probability = (victim_power / attacker_health) * 0.1  # Low but nonzero risk
        death_probability = min(0.3, death_probability)  # Max 30% death risk
        
        # Expected wallet gain (100% theft on kill)
        expected_gain = kill_probability * victim.resources.wallet
        
        # Expected wallet loss (if attacker dies, victim loots attacker)
        expected_loss = death_probability * attacker.resources.wallet
        
        # Net expected value
        expected_value = expected_gain - expected_loss
        
        return {
            "expected_value": expected_value,
            "kill_probability": kill_probability,
            "death_probability": death_probability,
            "expected_gain": expected_gain,
            "expected_loss": expected_loss
        }
    
    def calculate_sub_goal_amount(self, attacker, world_state):
        """
        Calculate attacker's minimum acceptable payment (sub-goal).
        
        Example: "I just need $10 to buy food, don't need to kill for full wallet"
        
        Returns: Minimum payment attacker would accept to retreat
        """
        # Check what attacker needs
        hunger = attacker.resources.hunger
        wallet = attacker.resources.wallet
        
        # Critical needs: Food to survive
        if hunger > 0.7:  # Very hungry
            # Need enough money to buy food (assume food costs ~$1-2)
            food_cost = 2.0
            return food_cost
        
        # Moderate needs: Refill wallet to comfort level
        elif wallet < 10.0:  # Low on cash
            target_wallet = 10.0
            needed = target_wallet - wallet
            return max(1.0, needed)
        
        # Greedy: Want more even if not desperate
        else:
            # Accept any significant payment (opportunistic mugging)
            return 5.0
    
    def should_accept_bribe(self, attacker, victim, bribe_amount):
        """
        Attacker decides: Accept bribe or reject and continue attacking?
        
        Decision factors:
        1. Is bribe >= expected value of killing victim?
        2. Does bribe satisfy attacker's sub-goal? (e.g., need $10 for food)
        3. Risk tolerance (conservative dots prefer safe bribe, aggressive dots gamble)
        
        Returns: (accept: bool, reason: str)
        """
        # Calculate expected value of attack
        ev_data = self.calculate_attack_expected_value(attacker, victim)
        attack_ev = ev_data["expected_value"]
        
        # Calculate minimum acceptable payment
        sub_goal = self.calculate_sub_goal_amount(attacker, None)
        
        # Decision logic
        
        # 1. Always accept if bribe >= expected attack value (rational choice)
        if bribe_amount >= attack_ev:
            return True, f"bribe_exceeds_ev (${bribe_amount:.2f} >= ${attack_ev:.2f})"
        
        # 2. Accept if bribe satisfies sub-goal AND attacker is risk-averse
        if bribe_amount >= sub_goal:
            # Risk tolerance based on attack gene (high attack = risk-seeking)
            risk_tolerance = attacker.dna.attack.points if attacker.dna.attack.enabled else 0
            
            if risk_tolerance < 10:  # Conservative (low attack investment)
                return True, f"sub_goal_satisfied (need ${sub_goal:.2f}, got ${bribe_amount:.2f})"
        
        # 3. Accept if attacker is desperate (very low wallet)
        if attacker.resources.wallet < 0.5 and bribe_amount > 0.5:
            return True, f"desperate (any money helps)"
        
        # 4. Reject if bribe too low compared to expected value
        if bribe_amount < attack_ev * 0.5:  # Less than half expected value
            return False, f"offer_too_low (${bribe_amount:.2f} < ${attack_ev:.2f} EV)"
        
        # 5. Aggressive dots reject unless guaranteed profit
        if risk_tolerance >= 15:  # Highly aggressive
            return False, f"aggressive_personality (prefer gambling for full wallet)"
        
        # Default: Accept if reasonable
        return True, f"reasonable_offer"
    
    def execute_instant_bribe(self, victim, attacker, bribe_amount):
        """
        Traditional one-time bribe offer.
        
        Victim offers lump sum, attacker decides accept/reject.
        
        Returns: dict with result
        """
        # Check if victim can afford
        if not victim.resources.has_money(bribe_amount):
            return {
                "result": "INSUFFICIENT_FUNDS",
                "requested": bribe_amount,
                "available": victim.resources.wallet
            }
        
        # Attacker decides
        accept, reason = self.should_accept_bribe(attacker, victim, bribe_amount)
        
        if accept:
            # Transfer money
            victim.resources.remove_money(bribe_amount)
            attacker.resources.add_money(bribe_amount)
            
            # Track stats
            victim.resources.bribes_paid += 1
            attacker.resources.bribes_received += 1
            victim.resources.peaceful_interactions += 1
            
            return {
                "result": "BRIBE_ACCEPTED",
                "amount": bribe_amount,
                "reason": reason,
                "attacker_id": attacker.id,
                "victim_id": victim.id
            }
        else:
            # Bribe rejected, combat continues
            return {
                "result": "BRIBE_REJECTED",
                "amount": bribe_amount,
                "reason": reason,
                "attacker_id": attacker.id,
                "victim_id": victim.id
            }
    
    def execute_mercy_mode(self, victim, attacker):
        """
        Activate wallet trickle (Mercy Dynamic).
        
        Victim opens wallet, money trickles to attacker over time.
        Attacker can choose to stop attacking once sub-goal satisfied.
        
        Returns: dict with result
        """
        # Activate trickle
        victim.resources.activate_mercy_mode(attacker.id)
        victim.current_state = "PAYING_TRIBUTE"
        
        return {
            "result": "MERCY_MODE_ACTIVATED",
            "victim_id": victim.id,
            "attacker_id": attacker.id
        }
    
    def should_continue_attack_during_mercy(self, attacker, victim):
        """
        Attacker decision: Keep attacking during mercy mode, or retreat?
        
        This is THE KEY MECHANIC for studying sub-lethal extortion.
        
        Returns: (continue_attack: bool, reason: str)
        """
        if not victim.resources.is_in_mercy_mode():
            return True, "no_mercy_mode"
        
        # How much has victim paid so far?
        total_paid = victim.resources.mercy_dynamic.total_paid
        
        # What's attacker's sub-goal?
        sub_goal = self.calculate_sub_goal_amount(attacker, None)
        
        # Has sub-goal been satisfied?
        if total_paid >= sub_goal:
            return False, f"sub_goal_satisfied (needed ${sub_goal:.2f}, got ${total_paid:.2f})"
        
        # Calculate expected value of killing for full wallet
        ev_data = self.calculate_attack_expected_value(attacker, victim)
        expected_kill_value = ev_data["expected_gain"]
        
        # Estimate remaining trickle value (assume 10 more ticks at ~$0.15/tick)
        estimated_trickle = total_paid + (0.15 * 10)
        
        # Risk-averse dots prefer safe trickle
        risk_tolerance = attacker.dna.attack.points if attacker.dna.attack.enabled else 0
        
        if risk_tolerance < 5:  # Very conservative
            if estimated_trickle > expected_kill_value * 0.3:
                return False, f"safe_income_preferred (trickle ~${estimated_trickle:.2f} vs risky ${expected_kill_value:.2f})"
        
        # Aggressive dots kill for full wallet
        if risk_tolerance >= 15:  # Highly aggressive
            return True, f"maximize_theft (want full ${victim.resources.wallet:.2f} wallet)"
        
        # If victim wallet running low, might as well kill
        if victim.resources.wallet < 2.0:
            return True, f"victim_nearly_broke (only ${victim.resources.wallet:.2f} left)"
        
        # Default: Continue extorting
        return True, f"continue_extortion"
    
    def execute(self, victim, attacker, bribe_amount=None, mode="instant"):
        """
        Main execution wrapper.
        
        Args:
            victim: Dot being attacked
            attacker: Dot doing the attacking
            bribe_amount: Amount to offer (instant mode only)
            mode: "instant" or "mercy"
        """
        if mode == "instant":
            if bribe_amount is None:
                # Calculate reasonable bribe (2x sub-goal)
                sub_goal = self.calculate_sub_goal_amount(attacker, None)
                bribe_amount = sub_goal * 2
            
            return self.execute_instant_bribe(victim, attacker, bribe_amount)
        
        elif mode == "mercy":
            return self.execute_mercy_mode(victim, attacker)
        
        else:
            return {"result": "INVALID_MODE", "mode": mode}


class GatherAction(Action):
    """
    DOT AI 3.0: Gather commodities from world.
    
    Physical collection of resources spawned in world.
    Free (no cost), but requires proximity to commodity.
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.range = self.calculate_range()
        self.speed = self.calculate_speed()
        super().__init__("gather", 0)  # Free action
    
    def calculate_range(self):
        """How close must be to gather"""
        return 20  # pixels (must be very close)
    
    def calculate_speed(self):
        """
        Gathering speed multiplier from DNA.
        Higher gather_speed gene = faster collection.
        
        Returns: time multiplier (1.0 = 1 second, 0.5 = 0.5 seconds)
        """
        base_speed = 1.0
        
        # Check if gather_speed gene exists (3.0 feature)
        if hasattr(self.dna, 'gather_speed') and self.dna.gather_speed.enabled:
            # Higher points = faster gathering
            speed_bonus = self.dna.gather_speed.points * 0.05  # 5% faster per point
            return base_speed / (1.0 + speed_bonus)
        
        return base_speed
    
    def can_execute(self, dot, world_state):
        """Can gather if inventory not full and commodity nearby"""
        # Check inventory space
        if dot.resources.is_inventory_full():
            return False
        
        # Check if market exists in world state
        if 'market' not in world_state:
            return False
        
        return True
    
    def execute(self, dot, commodity, market):
        """
        Gather a commodity from the world.
        
        Args:
            dot: Dot doing the gathering
            commodity: Commodity object to gather
            market: Market system reference
        
        Returns: dict with result
        """
        # Check range
        dx = commodity.position[0] - dot.position[0]
        dy = commodity.position[1] - dot.position[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > self.range:
            return {"result": "OUT_OF_RANGE", "distance": distance}
        
        # Check if already gathered
        if commodity.gathered:
            return {"result": "ALREADY_GATHERED"}
        
        # Check inventory space
        if dot.resources.is_inventory_full():
            return {"result": "INVENTORY_FULL"}
        
        # Gather commodity
        commodity_type, quantity = market.gather_commodity(commodity)
        
        if commodity_type is None:
            return {"result": "GATHER_FAILED"}
        
        # Add to inventory
        success = dot.resources.add_to_inventory(commodity_type, quantity)
        
        if not success:
            return {"result": "INVENTORY_FULL"}
        
        return {
            "result": "GATHERED",
            "commodity": commodity_type,
            "quantity": quantity,
            "gather_time": self.speed
        }


class BuyAction(Action):
    """
    DOT AI 3.0: Purchase commodities from market center.
    
    Costs money, adds to inventory.
    Price based on current market price (scarcity-driven).
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.price_discount = self.calculate_discount()
        super().__init__("buy", 0)  # No energy cost (just money)
    
    def calculate_discount(self):
        """
        Negotiation skill from DNA.
        Higher buy_power gene = better prices.
        
        Returns: discount percentage (0.0 to 0.25 max)
        """
        base_discount = 0.0
        
        # Check if buy_power gene exists (3.0 feature)
        if hasattr(self.dna, 'buy_power') and self.dna.buy_power.enabled:
            # Max 25% discount at 50 points
            skill_discount = self.dna.buy_power.points * 0.005
            return base_discount + min(0.25, skill_discount)
        
        return base_discount
    
    def can_execute(self, dot, world_state):
        """Can buy if have money and inventory space"""
        if dot.resources.wallet <= 0:
            return False
        
        if dot.resources.is_inventory_full():
            return False
        
        if 'market' not in world_state:
            return False
        
        return True
    
    def execute(self, dot, commodity_name, quantity, market):
        """
        Buy commodity from market.
        
        Args:
            dot: Dot doing the buying
            commodity_name: Type of commodity (e.g., "food_grain")
            quantity: How many to buy
            market: Market system reference
        
        Returns: dict with result
        """
        # Get market price
        base_price = market.get_price(commodity_name)
        
        if base_price == 0:
            return {"result": "INVALID_COMMODITY", "commodity": commodity_name}
        
        # Apply negotiation discount
        negotiated_price = base_price * (1.0 - self.price_discount)
        
        # Calculate total cost
        total_cost = negotiated_price * quantity
        
        # Check if can afford
        if not dot.resources.has_money(total_cost):
            return {
                "result": "INSUFFICIENT_FUNDS",
                "cost": total_cost,
                "wallet": dot.resources.wallet
            }
        
        # Check inventory space
        if dot.resources.get_inventory_count() + quantity > dot.resources.max_inventory_slots:
            return {"result": "INVENTORY_FULL"}
        
        # Execute purchase through market
        success, actual_cost = market.buy_from_market(commodity_name, quantity)
        
        if not success:
            return {"result": "OUT_OF_STOCK", "commodity": commodity_name}
        
        # Deduct money
        dot.resources.remove_money(total_cost)
        
        # Add to inventory
        dot.resources.add_to_inventory(commodity_name, quantity)
        
        # Track stats
        dot.resources.total_purchases += 1
        dot.resources.net_profit -= total_cost
        
        return {
            "result": "PURCHASE_SUCCESS",
            "commodity": commodity_name,
            "quantity": quantity,
            "price_per_unit": negotiated_price,
            "total_cost": total_cost,
            "discount_applied": self.price_discount
        }


class SellAction(Action):
    """
    DOT AI 3.0: Sell commodities to market center.
    
    Costs inventory, adds to wallet.
    Price based on current market price + negotiation bonus.
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.price_premium = self.calculate_premium()
        super().__init__("sell", 0)  # No energy cost
    
    def calculate_premium(self):
        """
        Negotiation skill from DNA.
        Higher sell_power gene = better prices.
        
        Returns: premium percentage (0.0 to 0.30 max)
        """
        base_premium = 0.0
        
        # Check if sell_power gene exists (3.0 feature)
        if hasattr(self.dna, 'sell_power') and self.dna.sell_power.enabled:
            # Max 30% premium at 50 points
            skill_premium = self.dna.sell_power.points * 0.006
            return base_premium + min(0.30, skill_premium)
        
        return base_premium
    
    def can_execute(self, dot, world_state):
        """Can sell if have items in inventory"""
        if dot.resources.get_inventory_count() == 0:
            return False
        
        if 'market' not in world_state:
            return False
        
        return True
    
    def execute(self, dot, commodity_name, quantity, market):
        """
        Sell commodity to market.
        
        Args:
            dot: Dot doing the selling
            commodity_name: Type of commodity
            quantity: How many to sell
            market: Market system reference
        
        Returns: dict with result
        """
        # Check if have item
        if not dot.resources.has_item(commodity_name, quantity):
            return {
                "result": "NO_ITEM",
                "commodity": commodity_name,
                "requested": quantity,
                "available": dot.resources.inventory.get(commodity_name, 0)
            }
        
        # Get market price
        base_price = market.get_price(commodity_name)
        
        if base_price == 0:
            return {"result": "INVALID_COMMODITY", "commodity": commodity_name}
        
        # Apply negotiation premium
        negotiated_price = base_price * (1.0 + self.price_premium)
        
        # Calculate total payment
        total_payment = negotiated_price * quantity
        
        # Check wallet capacity
        if dot.resources.wallet + total_payment > dot.resources.max_wallet:
            # Can still sell, just capped at max wallet
            actual_payment = min(total_payment, dot.resources.max_wallet - dot.resources.wallet)
        else:
            actual_payment = total_payment
        
        # Execute sale through market
        success, market_payment = market.sell_to_market(commodity_name, quantity)
        
        if not success:
            return {"result": "MARKET_ERROR"}
        
        # Remove from inventory
        dot.resources.remove_from_inventory(commodity_name, quantity)
        
        # Add money
        dot.resources.add_money(actual_payment)
        
        # Track stats
        dot.resources.total_sales += 1
        dot.resources.net_profit += actual_payment
        
        return {
            "result": "SALE_SUCCESS",
            "commodity": commodity_name,
            "quantity": quantity,
            "price_per_unit": negotiated_price,
            "total_payment": actual_payment,
            "premium_applied": self.price_premium
        }


class ConsumeAction(Action):
    """
    DOT AI 3.0: Consume food from inventory.
    
    Converts food items to energy.
    Different from 2.0 where food was world objects.
    Now food is inventory → energy.
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        super().__init__("consume", 0)  # Free action
    
    def can_execute(self, dot, world_state):
        """Can consume if have food in inventory"""
        # Check for any consumable item
        if 'market' not in world_state:
            return False
        
        market = world_state['market']
        
        for item_type in dot.resources.inventory.keys():
            if market.can_consume(item_type):
                return True
        
        return False
    
    def execute(self, dot, commodity_name, quantity, market):
        """
        Consume food from inventory.
        
        Args:
            dot: Dot doing the consuming
            commodity_name: Type of food
            quantity: How many to consume
            market: Market system reference (for energy values)
        
        Returns: dict with result
        """
        # Check if have item
        if not dot.resources.has_item(commodity_name, quantity):
            return {
                "result": "NO_ITEM",
                "commodity": commodity_name
            }
        
        # Check if consumable
        if not market.can_consume(commodity_name):
            return {
                "result": "NOT_CONSUMABLE",
                "commodity": commodity_name
            }
        
        # Get energy value
        energy_per_unit = market.get_energy_value(commodity_name)
        total_energy = energy_per_unit * quantity
        
        # Remove from inventory
        dot.resources.remove_from_inventory(commodity_name, quantity)
        
        # Add energy (using existing eat() method for cascading priority)
        if hasattr(dot, 'brain'):
            eat_result = dot.resources.eat(total_energy, dot.brain)
        else:
            # Fallback: just add energy
            dot.resources.add_energy(total_energy)
            eat_result = {"energy_gained": total_energy, "health_gained": 0, "dna_gained": 0}
        
        # Track stats
        dot.resources.total_consumed += 1
        
        return {
            "result": "CONSUMED",
            "commodity": commodity_name,
            "quantity": quantity,
            "energy_gained": eat_result.get("energy_gained", 0),
            "health_gained": eat_result.get("health_gained", 0),
            "dna_gained": eat_result.get("dna_gained", 0)
        }


class ActionManager:
    """Manages all available actions for a dot"""
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        
        # Initialize actions (2.0)
        self.attack = AttackAction(dna_profile)
        self.defend = DefendAction(dna_profile)
        self.replicate = ReplicateAction(dna_profile)
        
        # Initialize economic actions (3.0)
        self.bribe = BribeAction(dna_profile)
        self.gather = GatherAction(dna_profile)
        self.buy = BuyAction(dna_profile)
        self.sell = SellAction(dna_profile)
        self.consume = ConsumeAction(dna_profile)
    
    def get_available_actions(self, dot, world_state):
        """Get list of actions that can currently be executed"""
        available = []
        
        # Combat actions (2.0)
        if self.attack.can_execute(dot, world_state):
            available.append("attack")
        
        if self.defend.can_execute(dot, world_state):
            available.append("defend")
        
        if self.replicate.can_execute(dot, world_state):
            available.append("replicate")
        
        # Economic actions (3.0)
        if self.bribe.can_execute(dot, world_state):
            available.append("bribe")
        
        if self.gather.can_execute(dot, world_state):
            available.append("gather")
        
        if self.buy.can_execute(dot, world_state):
            available.append("buy")
        
        if self.sell.can_execute(dot, world_state):
            available.append("sell")
        
        if self.consume.can_execute(dot, world_state):
            available.append("consume")
        
        # Always available
        available.extend(["seek_food", "idle"])
        
        return available
