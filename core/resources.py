"""
Resource System - Energy, Health, and Hunger Management
Handles resource tracking, depletion, and regeneration

DOT AI 3.0 ADDITIONS:
- Economic resources (wallet, inventory)
- Mercy Dynamic (wallet trickle bribery system)
- Transaction history tracking
- Behavior classification
"""

class MercyDynamic:
    """
    Wallet trickle bribery system
    Victim can 'open wallet' during attack, trickling money to attacker
    Attacker can choose to stop attacking once sub-goal satisfied
    
    Research Question: Do dots develop sub-lethal extortion vs murder?
    """
    
    def __init__(self):
        self.is_active = False
        self.trickle_rate_min = 0.05  # $0.05 per tick (minimum)
        self.trickle_rate_max = 0.20  # $0.20 per tick (maximum)
        self.trickle_interval = 0.5   # Every 0.5 seconds
        self.total_paid = 0.0
        self.time_since_last_trickle = 0.0
        self.attacker_id = None
    
    def activate(self, attacker_id):
        """Victim opens wallet, begins trickle"""
        self.is_active = True
        self.attacker_id = attacker_id
        self.total_paid = 0.0
        self.time_since_last_trickle = 0.0
        print(f"[MERCY] Wallet opened for attacker {attacker_id}")
    
    def deactivate(self):
        """Exit bribery mode (fight or flight)"""
        print(f"[MERCY] Exiting mercy mode. Total paid: ${self.total_paid:.2f}")
        self.is_active = False
        self.attacker_id = None
    
    def update(self, dt, victim_wallet):
        """
        Process trickle payment
        Returns: dict with payment info if trickle occurred, None otherwise
        """
        if not self.is_active:
            return None
        
        self.time_since_last_trickle += dt
        
        # Trickle money at interval
        if self.time_since_last_trickle >= self.trickle_interval:
            # Random payment amount (simulates fumbling for bills)
            import random
            trickle_amount = random.uniform(self.trickle_rate_min, self.trickle_rate_max)
            
            # Can't pay more than wallet has
            actual_payment = min(trickle_amount, victim_wallet)
            
            if actual_payment > 0:
                # Transfer money
                self.total_paid += actual_payment
                self.time_since_last_trickle = 0.0
                
                return {
                    "payment": actual_payment,
                    "total_paid": self.total_paid,
                    "attacker_id": self.attacker_id
                }
            else:
                # Wallet empty, deactivate
                self.deactivate()
        
        return None


class Resources:
    """
    Manages a dot's vital resources
    
    SURVIVAL RESOURCES (Dot AI 2.0):
    - Energy: Primary fuel for actions
    - Health: Life force, death at 0
    - Hunger: Derived from energy ratio
    
    ECONOMIC RESOURCES (Dot AI 3.0):
    - Wallet: Cash/currency for trading
    - Inventory: Tradable items (food, materials)
    - Transaction history
    - Mercy Dynamic state
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        
        # ===== SURVIVAL RESOURCES (2.0) =====
        # Energy
        self.max_energy = self.calculate_max_energy()
        self.energy = self.max_energy * 0.6  # Start at 60% energy (hungry!)
        
        # Health
        self.max_health = 100  # Base value (may add DNA scaling later)
        self.health = self.max_health  # Start full
        
        # Hunger (derived, not stored separately in simple model)
        self.hunger = 0.0  # 0 = satisfied, 1 = starving
        
        # ===== ECONOMIC RESOURCES (3.0) =====
        # Wallet
        self.wallet = 5.0  # Start with $5
        self.max_wallet = self.calculate_max_wallet()
        
        # Inventory (tradable items)
        self.inventory = {}  # {"food_grain": 2, "iron": 1, "scrap": 3}
        self.max_inventory_slots = 10  # Limited carrying capacity
        
        # ===== MERCY DYNAMIC (3.0) =====
        self.mercy_dynamic = MercyDynamic()
        
        # ===== TRANSACTION HISTORY (3.0) =====
        self.total_purchases = 0
        self.total_sales = 0
        self.total_consumed = 0
        self.net_profit = 0.0
        self.bribes_paid = 0
        self.bribes_received = 0
        
        # ===== QUALITY OF LIFE TRACKING (3.0) =====
        self.attack_count = 0  # Times attacked by others
        self.peaceful_interactions = 0  # Successful peaceful trades/bribes
        self.kills = 0  # Dots killed by this dot
        self.deaths_caused_by = None  # ID of killer (for analytics)
        
        # ===== BEHAVIOR CLASSIFICATION (3.0) =====
        self.behavior_class = "Newborn"  # Updated based on actions
        self.violence_pattern = "unknown"  # "never", "defensive", "opportunistic", "aggressive"
        self.economic_pattern = "unknown"  # "trader", "investor", "hoarder", "scavenger"
    
    def calculate_max_energy(self):
        """
        Calculate maximum energy from DNA
        Base: 100
        DNA Bonus: movement_max_energy gene_points * 5
        """
        base = 100
        if self.dna.movement_max_energy.enabled:
            bonus = self.dna.movement_max_energy.points * 5
            return base + bonus
        return base
    
    def calculate_max_wallet(self):
        """
        Calculate wallet capacity from health
        Base: max_health (1:1 ratio)
        DNA Bonus: max_wallet gene if exists (10 points per gene_point)
        """
        base_capacity = self.max_health
        
        # Check if max_wallet gene exists (3.0 feature)
        if hasattr(self.dna, 'max_wallet') and self.dna.max_wallet.enabled:
            bonus = self.dna.max_wallet.points * 10
            return base_capacity + bonus
        
        return base_capacity
    
    # ===== ECONOMIC METHODS (3.0) =====
    
    def add_money(self, amount):
        """Add money to wallet (capped at max_wallet)"""
        old_wallet = self.wallet
        self.wallet = min(self.max_wallet, self.wallet + amount)
        actual_added = self.wallet - old_wallet
        return actual_added
    
    def remove_money(self, amount):
        """
        Remove money from wallet
        Returns: actual amount removed (may be less if insufficient funds)
        """
        actual_removed = min(amount, self.wallet)
        self.wallet -= actual_removed
        return actual_removed
    
    def has_money(self, amount):
        """Check if wallet has at least this much money"""
        return self.wallet >= amount
    
    def add_to_inventory(self, item_type, quantity=1):
        """Add items to inventory (if space available)"""
        # Check capacity
        current_items = sum(self.inventory.values())
        if current_items + quantity > self.max_inventory_slots:
            return False  # Inventory full
        
        # Add items
        if item_type in self.inventory:
            self.inventory[item_type] += quantity
        else:
            self.inventory[item_type] = quantity
        
        return True
    
    def remove_from_inventory(self, item_type, quantity=1):
        """Remove items from inventory"""
        if item_type not in self.inventory:
            return False
        
        if self.inventory[item_type] < quantity:
            return False
        
        self.inventory[item_type] -= quantity
        
        # Clean up if quantity reaches 0
        if self.inventory[item_type] == 0:
            del self.inventory[item_type]
        
        return True
    
    def has_item(self, item_type, quantity=1):
        """Check if inventory contains item"""
        return self.inventory.get(item_type, 0) >= quantity
    
    def get_inventory_count(self):
        """Get total items in inventory"""
        return sum(self.inventory.values())
    
    def is_inventory_full(self):
        """Check if inventory at capacity"""
        return self.get_inventory_count() >= self.max_inventory_slots
    
    def update_mercy_dynamic(self, dt):
        """
        Update mercy dynamic trickle payment
        Returns: payment info if trickle occurred
        """
        if not self.mercy_dynamic.is_active:
            return None
        
        # Process trickle
        result = self.mercy_dynamic.update(dt, self.wallet)
        
        if result and result["payment"] > 0:
            # Deduct from wallet
            self.wallet -= result["payment"]
            self.bribes_paid += 1
            print(f"[MERCY] Trickle payment: ${result['payment']:.2f} (Total: ${result['total_paid']:.2f})")
            return result
        
        return None
    
    def activate_mercy_mode(self, attacker_id):
        """Enter bribery mode (open wallet)"""
        self.mercy_dynamic.activate(attacker_id)
    
    def deactivate_mercy_mode(self):
        """Exit bribery mode (fight or flight)"""
        self.mercy_dynamic.deactivate()
    
    def is_in_mercy_mode(self):
        """Check if currently in mercy mode"""
        return self.mercy_dynamic.is_active
    
    # ===== HOLD POWER / INTEREST SYSTEM (3.0) =====
    
    def calculate_interest_rate(self):
        """
        Calculate wallet interest rate based on hold_power gene
        
        Base rate: 0.05% per second (0.0005)
        Gene bonus: 0.01% per point (0.0001 per point)
        Max bonus: 50 points = +0.5% per second
        
        Returns:
            Interest rate as decimal (e.g., 0.001 = 0.1% per second)
        """
        base_rate = 0.0005  # 0.05% per second
        
        # Check if hold_power gene exists (3.0 feature)
        if hasattr(self.dna, 'hold_power') and self.dna.hold_power.enabled:
            gene_bonus = self.dna.hold_power.points * 0.0001  # 0.01% per point
            return base_rate + gene_bonus
        
        return base_rate
    
    def apply_interest(self, dt):
        """
        Apply interest to wallet balance based on hold_power gene
        
        Interest compounds continuously at the rate specified by calculate_interest_rate().
        This simulates "passive income" for investor-type dots.
        
        Args:
            dt: Time delta in seconds since last update
        
        Returns:
            dict with:
            - interest_earned: Amount of money earned from interest
            - new_balance: Wallet balance after interest
            - rate_used: Interest rate applied
        """
        # Only earn interest if wallet has money
        if self.wallet <= 0:
            return {
                'interest_earned': 0.0,
                'new_balance': 0.0,
                'rate_used': 0.0
            }
        
        # Calculate interest
        rate = self.calculate_interest_rate()
        interest = self.wallet * rate * dt
        
        # Apply interest (capped at max_wallet)
        old_wallet = self.wallet
        actual_interest = self.add_money(interest)
        
        return {
            'interest_earned': actual_interest,
            'new_balance': self.wallet,
            'rate_used': rate,
            'was_capped': actual_interest < interest
        }
    
    def get_passive_income_per_minute(self):
        """
        Calculate projected passive income per minute at current wallet balance
        
        Returns:
            Expected income per minute from interest
        """
        rate = self.calculate_interest_rate()
        income_per_second = self.wallet * rate
        income_per_minute = income_per_second * 60
        return income_per_minute
    
    # ===== SURVIVAL METHODS (2.0) =====
    
    def update_hunger(self):
        """
        Recalculate hunger based on energy ratio
        Hunger = 1 - (current_energy / max_energy)
        """
        self.hunger = 1.0 - (self.energy / self.max_energy)
    
    def deplete_energy(self, amount):
        """
        Remove energy (movement, actions, idle)
        Energy cannot go below 0
        """
        self.energy = max(0.0, self.energy - amount)
        self.update_hunger()
    
    def add_energy(self, amount):
        """
        Add energy (from eating)
        Energy cannot exceed max
        Returns: Amount of overflow (for DNA conversion)
        """
        old_energy = self.energy
        self.energy = min(self.max_energy, self.energy + amount)
        self.update_hunger()
        
        # Return overflow amount
        overflow = amount - (self.energy - old_energy)
        return max(0.0, overflow)
    
    def deplete_health(self, amount):
        """
        Damage health (from starvation, attacks)
        Health cannot go below 0
        """
        self.health = max(0.0, self.health - amount)
    
    def add_health(self, amount):
        """
        Heal health (from energy overflow)
        Health cannot exceed max
        Returns: Amount of overflow (for DNA conversion)
        """
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        
        # Return overflow amount
        overflow = amount - (self.health - old_health)
        return max(0.0, overflow)
    
    def eat(self, food_energy: float, brain):
        """
        Consume food with cascading priority system:
        1. Fill energy first
        2. Overflow goes to health
        3. When both full, overflow converts to DNA points (10% conversion rate)
        
        Args:
            food_energy: Energy value from food
            brain: Brain reference for DNA growth
        
        Returns: Dict with energy_gained, health_gained, dna_gained
        """
        result = {'energy_gained': 0, 'health_gained': 0, 'dna_gained': 0}
        
        # Priority 1: Fill energy
        energy_overflow = self.add_energy(food_energy)
        result['energy_gained'] = food_energy - energy_overflow
        
        # Priority 2: Overflow goes to health (if any)
        if energy_overflow > 0:
            health_overflow = self.add_health(energy_overflow)
            result['health_gained'] = energy_overflow - health_overflow
            
            # Priority 3: When both full, convert to DNA (10% conversion)
            if health_overflow > 0:
                # 10% of overflow becomes DNA points (prevents runaway growth)
                dna_gain = health_overflow * 0.10
                brain.dna.earn_dna_points(dna_gain)
                result['dna_gained'] = dna_gain
        
        return result
    
    def is_alive(self):
        """Check if dot is alive (health > 0)"""
        return self.health > 0
    
    def is_starving(self):
        """Check if in starvation state (energy = 0 but health > 0)"""
        return self.energy <= 0 and self.health > 0
    
    def is_satiated(self):
        """Check if energy is maxed out (for DNA point gain)"""
        return self.energy >= self.max_energy
    
    def is_healthy(self):
        """Check if health is maxed out (for ability unlocking)"""
        return self.health >= self.max_health
    
    def get_energy_ratio(self):
        """Get energy as ratio 0-1"""
        return self.energy / self.max_energy if self.max_energy > 0 else 0
    
    def get_health_ratio(self):
        """Get health as ratio 0-1"""
        return self.health / self.max_health if self.max_health > 0 else 0
    
    def serialize(self):
        """Export resource state (2.0 + 3.0 fields)"""
        return {
            # Survival resources (2.0)
            'energy': self.energy,
            'max_energy': self.max_energy,
            'energy_ratio': self.get_energy_ratio(),
            'health': self.health,
            'max_health': self.max_health,
            'health_ratio': self.get_health_ratio(),
            'hunger': self.hunger,
            'is_alive': self.is_alive(),
            'is_starving': self.is_starving(),
            'is_satiated': self.is_satiated(),
            
            # Economic resources (3.0)
            'wallet': self.wallet,
            'max_wallet': self.max_wallet,
            'inventory': self.inventory.copy(),
            'inventory_count': self.get_inventory_count(),
            'is_inventory_full': self.is_inventory_full(),
            
            # Mercy dynamic (3.0)
            'mercy_mode_active': self.mercy_dynamic.is_active,
            'mercy_total_paid': self.mercy_dynamic.total_paid,
            
            # Transaction history (3.0)
            'total_purchases': self.total_purchases,
            'total_sales': self.total_sales,
            'net_profit': self.net_profit,
            'bribes_paid': self.bribes_paid,
            'bribes_received': self.bribes_received,
            'peaceful_interactions': self.peaceful_interactions,
            
            # Violence tracking (3.0)
            'attack_count': self.attack_count,
            'kills': self.kills,
            
            # Behavior classification (3.0)
            'behavior_class': self.behavior_class,
            'violence_pattern': self.violence_pattern,
            'economic_pattern': self.economic_pattern
        }
    
    def __repr__(self):
        return f"Resources(E:{self.energy:.0f}/{self.max_energy:.0f}, H:{self.health:.0f}/{self.max_health:.0f}, $:{self.wallet:.2f})"
