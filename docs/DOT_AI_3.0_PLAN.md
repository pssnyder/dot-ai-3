# 🌍 Dot AI 3.0: Economic Simulation - Project Plan

**Date Created:** January 9, 2026  
**Status:** Planning Phase  
**Evolution:** Dot AI 2.0 (Combat/Survival) → Dot AI 3.0 (Economic Ecosystem)

---

## 🎯 Vision Statement

**Dot AI 3.0** transforms the survival simulation into an **economic ecosystem** where dots compete through commerce, not combat. Instead of fighting for food, dots will **buy, sell, hold, and merge** in a dynamic market economy. Success is measured by wealth accumulation, credit scores, and strategic mergers rather than combat victories.

**Core Philosophy:**
- Same AI principles (DNA-based evolution, utility-driven decisions)
- Different survival mechanics (economic instead of physical)
- New emergent behaviors (market strategies, trading patterns, economic niches)

---

## 📊 Core Concept Transformation

### **🔄 Hybrid Survival-Economic System**

**Key Innovation:** Resources serve **dual purposes** - survival AND trade. Dots must decide: *consume or sell?* This creates emergent economic strategy where survival needs compete with wealth accumulation.

| **Dot AI 2.0 (Combat)**          | **Dot AI 3.0 (Economic)**                    |
|----------------------------------|----------------------------------------------|
| **Food**                         | **Food** (eat for energy OR sell for money)  |
| **Energy**                       | **Energy** (survival) + **Wallet** (money)   |
| **Health**                       | **Health** (survival capacity = bank size)   |
| **Attack Action**                | **Buy Action** (acquire resources)           |
| **Defend Action**                | **Hold Action** (save/invest)                |
| **Replicate (Reproduce)**        | **Merge & Acquire** (M&A)                    |
| **Seek Food**                    | **Seek Resources** (survival + trade)        |
| **Combat Range**                 | **Trading Reach**                            |
| **Starvation Death**             | **Starvation** (no energy) OR **Bankruptcy** |
| **Death → Food Conversion**      | **Death → Asset Liquidation** (inventory drops) |
| **Damage/Combat**                | **Price Negotiation**                        |
| **Offspring (Sexual/Asexual)**   | **Merged Companies** (two dots combine)      |
| **DNA Budget (fixed)**           | **DNA Budget** (expandable via purchases!)   |

### **💡 The Economic-Survival Loop**

```
┌─────────────────────────────────────────────────────────┐
│  GATHER FOOD → Decide: EAT or SELL?                     │
│                                                          │
│  ┌──────────┐              ┌─────────────┐              │
│  │   EAT    │              │    SELL     │              │
│  └────┬─────┘              └──────┬──────┘              │
│       │                           │                     │
│       ▼                           ▼                     │
│  +Energy (survive)           +Money (wealth)            │
│                                   │                     │
│                                   ▼                     │
│                        BUY UPGRADES (DNA, memory)       │
│                                   │                     │
│                                   ▼                     │
│                        STRONGER ABILITIES               │
│                                   │                     │
│                                   ▼                     │
│                        GATHER MORE EFFICIENTLY          │
└─────────────────────────────────────────────────────────┘
```

**Strategic Tension:**
- **Survival First:** Starving dots must eat, can't build wealth
- **Wealth Building:** Well-fed dots can sell food for upgrades
- **Investment Payoff:** Upgraded dots gather resources faster
- **Market Dynamics:** If everyone hoards food, prices skyrocket

### **🏦 Commodity-Focused Economy (No Physical Combat)**

**Key Design Decision:** Dots compete through **economic warfare**, not physical combat. All conflict happens "on paper" through market manipulation, resource hoarding, and strategic trading.

**Commodity Categories:**

1. **Food (3 types - survival need with different nutritional values)**
   - **Grain:** Low nutrition (+20 energy), high spawn rate, cheap ($10)
   - **Fruit:** Medium nutrition (+35 energy), moderate spawn, medium price ($18)
   - **Meat:** High nutrition (+50 energy), rare spawn, expensive ($30)
   
2. **Precious Metals (pure value storage)**
   - **Silver:** Stable value storage, low volatility ($40)
   - **Gold:** Premium value storage, crisis hedge ($80)
   
3. **Lifestyle Goods (demand tied to population/activity)**
   - **Clothing:** Demand scales linearly with population ($15)
   - **Paper:** Complex recycling mechanics (demand cycles) ($12)
   
4. **Upgrades (consume for permanent benefits)**
   - **DNA Serum:** +10 DNA points (expand abilities)
   - **Memory Chip:** +5 memory slots (better decisions)
   - **Medical Kit:** +20 max health (bigger wallet capacity)
   - **Energy Core:** +20 max energy (bigger inventory)

**Market Dynamics:**
- **Survival-driven:** Food demand spikes when average energy is low
- **Population-driven:** Clothing demand = population × 0.5
- **Fear-driven:** Gold/silver demand rises with market volatility
- **Recycling mechanics:** Paper supply cycles (scarcity → abundance → scarcity)
- **Wealth-gated:** Upgrade demand from wealthy dots only

**Economic Competition Mechanics:**
- **Resource race:** Fast gatherers get commodities first
- **Market timing:** Buy low (surplus), sell high (scarcity)
- **Hoarding:** Control supply to drive up prices
- **Dumping:** Flood market to crash prices (hurt competitors)
- **Bankruptcy warfare:** Drive competitors to $0 balance

---

## 🧬 1. DNA System Transformation

### File: `core/dna.py`

#### **Gene Category Mapping**

**🧠 BRAIN GENES** (Cognitive Capacity):
| Old Name | New Name | Purpose |
|----------|----------|---------|
| `brain_memory` | `transaction_memory` | Remember past trades, prices, partners |
| `brain_sense_slots` | `market_analysis_slots` | Number of market factors can analyze |
| `brain_action_slots` | `strategy_slots` | Number of trading strategies can consider |

**👁️ SENSE GENES** (Market Perception):
| Old Name | New Name | Purpose |
|----------|----------|---------|
| `vision_distance` | `market_visibility` | How far can detect goods/traders |
| `vision_fov` | `market_fov` | Field of view for market scanning |
| `dot_detection` | `trader_detection` | Ability to sense other trading dots |
| `food_detection` | `goods_detection` | Ability to locate tradable goods |
| `dna_strength_detection` | `wealth_detection` | Identify rich vs poor traders |

**💰 ACTION GENES** (Economic Actions):
| Old Name | New Name | Purpose |
|----------|----------|---------|
| `movement_speed` | `movement_speed` | Navigate to trading opportunities |
| `attack` | `buy_power` | Purchasing efficiency (negotiate lower buy prices) |
| `defend` | `sell_power` | Selling efficiency (negotiate higher sell prices) |
| `replicate` | `merge_ability` | M&A capability (combine with other dots) |
| **NEW** | `gather_speed` | How quickly can collect resources from world |
| **NEW** | `hold_power` | Saving/investment capability (earn interest) |

**Note:** No combat genes! Competition happens through economic means:
- Outbid competitors for scarce resources
- Manipulate markets through hoarding/dumping
- Drive others to bankruptcy through market control

#### **DNA Budget System** (Unchanged Philosophy)
- Default: **100 points** starting budget
- Dots must specialize (can't max all genes)
- Creates economic niches:
  - **Traders:** High buy/sell, low hold
  - **Investors:** High hold, low buy/sell
  - **Scouts:** High visibility, find deals
  - **Conglomerates:** High merge, build empires

---

## 💰 2. Resources System Transformation

### File: `core/resources.py` (KEEP, but enhance)

#### **Hybrid Resource Structure**

**Philosophy:** Dots still need energy to survive, but now they also have money to trade. Health and energy maxes determine storage capacity (like bank size). This creates economic progression tied to biological fitness.

```python
class HybridResources:
    """
    Manages dot's survival AND economic state
    Survival resources (energy, health) + Economic resources (wallet, inventory)
    """
    
    # ===== SURVIVAL RESOURCES (from 2.0) =====
    energy: float              # Current energy (0-100 default)
    max_energy: float          # Energy capacity (DNA-based)
    health: float              # Current health (0-100 default)
    max_health: float          # Health capacity (DNA-based)
    
    # ===== ECONOMIC RESOURCES (new in 3.0) =====
    wallet: float              # Money/currency (separate from energy!)
    max_wallet: float          # Wallet capacity = max_health (bank size)
    
    # ===== INVENTORY SYSTEM =====
    # Food and materials can be consumed OR sold
    inventory: Dict[str, int]  # {"food": 5, "wood": 3, "tools": 1}
    max_inventory: int         # Capacity = max_energy / 10
    
    # ===== ECONOMIC STATE =====
    bankrupt: bool             # Wallet ≤ 0 AND energy ≤ 0
    bankruptcy_timer: float    # Grace period before removal
    
    # ===== TRANSACTION HISTORY =====
    total_purchases: int       # Bought items
    total_sales: int           # Sold items
    total_consumed: int        # Ate food
    net_profit: float          # Money earned - spent
```

#### **Key Resource Mechanics**

**1. Energy (Survival Primary)**
```python
# Still depletes over time (like 2.0)
energy -= IDLE_COST * dt
energy -= MOVEMENT_COST * dt if moving

# Can be restored by:
# - Eating food from inventory (consume)
# - OR buying food and eating it

# Starvation still kills
if energy <= 0:
    health -= STARVATION_DAMAGE * dt
```

**2. Health (Determines Bank Size)**
```python
# Health = biological fitness
# Higher health = larger wallet capacity
max_wallet = max_health  # 1:1 ratio

# Example:
# Dot with 100 health → Can store $100 max
# Dot with 150 health → Can store $150 max

# Health damaged by:
# - Starvation (energy = 0)
# - (No combat in 3.0)

# Health restored by:
# - Consuming food (small health boost)
# - Buying "medical kits" (luxury item)
```

**3. Wallet (Economic Primary)**
```python
# Separate currency pool
# Used for buying/selling
# Cannot exceed max_wallet (health-limited)

# Earned by:
# - Selling inventory items
# - Holding (interest on savings)

# Spent on:
# - Buying food (eat to survive)
# - Buying materials (trade for profit)
# - Buying UPGRADES (DNA expansion!)
```

**4. Inventory (Dual-Purpose Storage)**
```python
# Stores items with dual utility:
INVENTORY_ITEMS = {
    # SURVIVAL ITEMS (can consume OR sell)
    "food": {
        "consume_effect": "+30 energy, +5 health",
        "sell_price": "$10 base"
    },
    
    # TRADE MATERIALS (can only sell)
    "wood": {
        "consume_effect": None,
        "sell_price": "$8 base"
    },
    "metal": {
        "consume_effect": None,
        "sell_price": "$20 base"
    },
    
    # LUXURY ITEMS (high value trade)
    "gems": {
        "consume_effect": None,
        "sell_price": "$50 base"
    },
    
    # UPGRADE ITEMS (consume for permanent benefits)
    "dna_serum": {
        "consume_effect": "+10 DNA points",
        "sell_price": "$100 base"
    },
    "memory_chip": {
        "consume_effect": "+5 memory slots",
        "sell_price": "$80 base"
    },
    "medical_kit": {
        "consume_effect": "+20 health (increase max_health)",
        "sell_price": "$60 base"
    },
    "energy_core": {
        "consume_effect": "+20 max_energy (bigger bank)",
        "sell_price": "$60 base"
    }
}
```

#### **Economic Survival Mechanics**

**Bankruptcy System** (Replaces Starvation):
```python
# Constants
BANKRUPTCY_GRACE_PERIOD = 5.0  # Seconds before bankruptcy
OPERATIONAL_COST_BASE = 1.0    # Money/second (like idle energy)
MOVEMENT_COST = 0.5            # Additional cost when moving

# Logic
if wallet_balance <= 0:
    bankruptcy_timer += dt
    if bankruptcy_timer >= BANKRUPTCY_GRACE_PERIOD:
        # Dot goes bankrupt → Remove from simulation
        # Assets liquidated → Spawn goods at position
        return "BANKRUPT"
```

**Credit Score System** (Replaces Health):
```python
# Credit score affects:
# - Merge eligibility (need high credit to merge)
# - Buy/sell prices (low credit = worse deals)
# - Interest rates (high credit = better returns on Hold)

# Credit improves with:
# - Successful trades (+2 per trade)
# - Positive balance (+0.5 per second if balance > 50%)
# - Mergers (+10 if merger succeeds)

# Credit decreases with:
# - Failed trades (-5 per failed attempt)
# - Low balance (-1 per second if balance < 20%)
# - Bankruptcy approach (-3 per second if balance = 0)
```

**Operational Costs** (Replaces Energy Depletion):
```python
# All dots have baseline "burn rate"
idle_cost = OPERATIONAL_COST_BASE * dt
movement_cost = MOVEMENT_COST * dt if is_moving else 0
action_cost = action_specific_cost  # Buy/sell/hold have different costs

total_cost = idle_cost + movement_cost + action_cost
wallet_balance -= total_cost
```

---

## 🎯 3. Actions System Transformation

### File: `core/actions.py`

**Philosophy:** All interactions are economic. No physical combat - dots compete through:
- **Market competition:** Buy low, sell high
- **Resource hoarding:** Control supply to manipulate prices
- **Strategic trading:** Exploit market inefficiencies
- **Economic warfare:** Drive competitors to bankruptcy

#### **GatherAction** (Replaces AttackAction - Primary resource collection)

```python
class GatherAction(Action):
    """
    Pick up resources from the world (free, but takes time)
    Speed depends on gather_speed gene
    Primary way to acquire commodities
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.gather_range = 20  # Can pick up items within 20px
        self.gather_speed = 1.0 + (dna_profile.gather_speed.points * 0.02)  # 1.0 to 2.0x speed
        super().__init__("gather", 0)  # Free action
    
    def execute(self, dot, resource, delta_time):
        """Pick up resource from world"""
        # Check if in range
        distance = get_distance(dot.position, resource.position)
        if distance > self.gather_range:
            return {"result": "OUT_OF_RANGE"}
        
        # Check inventory space
        if dot.resources.is_inventory_full():
            return {"result": "INVENTORY_FULL"}
        
        # Gather with speed multiplier (faster gathering = competitive advantage)
        gather_time = 1.0 / self.gather_speed  # Base 1 second, faster with gene
        
        # Add to inventory
        dot.resources.add_to_inventory(resource.type, resource.quantity)
        
        return {
            "result": "GATHERED",
            "item": resource.type,
            "quantity": resource.quantity
        }


class BuyAction(Action):
    """
    Purchase commodities from market center at current market price
    Cost depends on buy_power gene (negotiation skill for better prices)
    Secondary way to acquire commodities (costs money)
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.range = self.calculate_trading_range()
        self.price_discount = self.calculate_discount()
        super().__init__("buy", 0)  # Cost varies by item
    
    def calculate_trading_range(self):
        """How far can initiate trades"""
        base = 40  # pixels
        bonus = self.dna.buy_power.points * 3
        return base + bonus
    
    def calculate_discount(self):
        """Better negotiators pay less"""
        base_discount = 0.0
        skill_discount = self.dna.buy_power.points * 0.005  # Max 25% off
        return base_discount + skill_discount
    
    def execute(self, dot, good, delta_time):
        """Buy a good from the market"""
        # Calculate final price
        base_price = good.base_value
        market_modifier = good.demand_multiplier
        negotiated_price = base_price * market_modifier * (1.0 - self.price_discount)
        
        # Credit score affects price (bad credit = premium)
        credit_modifier = 1.0 + (0.5 * (1.0 - dot.resources.credit_score / 100))
        final_price = negotiated_price * credit_modifier
        
        # Check if can afford
        if dot.resources.wallet_balance < final_price:
            return {"result": "INSUFFICIENT_FUNDS"}
        
        # Check inventory space
        if dot.resources.is_inventory_full():
            return {"result": "INVENTORY_FULL"}
        
        # Execute purchase
        dot.resources.wallet_balance -= final_price
        dot.resources.add_to_inventory(good.type, 1)
        dot.resources.credit_score += 2  # Successful trade
        dot.resources.total_purchases += 1
        
        return {
            "result": "PURCHASE_SUCCESS",
            "item": good.type,
            "price": final_price
        }
```

#### **SellAction** (NEW)

```python
class SellAction(Action):
    """
    Sell goods from inventory to market
    Price depends on sell_power gene
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.price_premium = self.calculate_premium()
        super().__init__("sell", 0)
    
    def calculate_premium(self):
        """Better sellers get more money"""
        base_premium = 0.0
        skill_premium = self.dna.sell_power.points * 0.006  # Max 30% bonus
        return base_premium + skill_premium
    
    def execute(self, dot, good_type, delta_time):
        """Sell an item from inventory"""
        # Check if have item
        if not dot.resources.has_in_inventory(good_type):
            return {"result": "NO_ITEM"}
        
        # Calculate sale price
        base_price = GOOD_BASE_PRICES[good_type]
        market_modifier = get_market_demand(good_type)
        negotiated_price = base_price * market_modifier * (1.0 + self.price_premium)
        
        # Credit affects price (high credit = better deals)
        credit_bonus = (dot.resources.credit_score / 100) * 0.3
        final_price = negotiated_price * (1.0 + credit_bonus)
        
        # Execute sale
        dot.resources.remove_from_inventory(good_type, 1)
        dot.resources.wallet_balance += final_price
        dot.resources.credit_score += 2
        dot.resources.total_sales += 1
        dot.resources.net_profit += final_price
        
        return {
            "result": "SALE_SUCCESS",
            "item": good_type,
            "price": final_price
        }
```

#### **HoldAction** (Replaces DefendAction)

```python
class HoldAction(Action):
    """
    Hold cash and earn interest (passive income)
    Trade-off: Can't buy/sell while holding
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        self.interest_rate = self.calculate_interest_rate()
        super().__init__("hold", 0)
    
    def calculate_interest_rate(self):
        """Better holders earn more interest"""
        base_rate = 0.005  # 0.5% per second
        skill_bonus = self.dna.hold_power.points * 0.0001  # Up to +0.5%
        return base_rate + skill_bonus
    
    def execute(self, dot, world_state, delta_time):
        """Generate passive income from holdings"""
        # Can only hold if have significant balance
        if dot.resources.wallet_balance < 20:
            return {"result": "INSUFFICIENT_BALANCE"}
        
        # Calculate interest earned
        interest = dot.resources.wallet_balance * self.interest_rate * delta_time
        
        # Credit score affects returns (high credit = better rates)
        credit_multiplier = 0.5 + (dot.resources.credit_score / 100) * 0.5
        final_interest = interest * credit_multiplier
        
        # Apply earnings
        dot.resources.wallet_balance += final_interest
        dot.is_holding = True  # Set state flag
        
        return {
            "result": "HOLDING",
            "interest_earned": final_interest,
            "rate": self.interest_rate * credit_multiplier
        }
```

#### **MergeAction** (Replaces ReplicateAction)

```python
class MergeAction(Action):
    """
    Merge & Acquisition - Two dots combine into one stronger entity
    Sexual reproduction equivalent in economic simulation
    """
    
    def __init__(self, dna_profile):
        self.dna = dna_profile
        super().__init__("merge", 0)
    
    def can_execute(self, dot_a, dot_b):
        """Requirements for merger"""
        # Both must have merge ability
        if not (dot_a.dna.merge_ability.enabled and dot_b.dna.merge_ability.enabled):
            return False
        
        # Both must have sufficient capital (60%+ of max)
        if dot_a.resources.wallet_balance < dot_a.resources.max_balance * 0.6:
            return False
        if dot_b.resources.wallet_balance < dot_b.resources.max_balance * 0.6:
            return False
        
        # Both must have good credit (70%+)
        if dot_a.resources.credit_score < 70 or dot_b.resources.credit_score < 70:
            return False
        
        return True
    
    def execute(self, parent_a, parent_b, world_state):
        """Execute merger - create new combined entity"""
        from .dna import DNAProfile
        
        # Merger costs: 40% of each dot's balance (transaction fees)
        cost_a = parent_a.resources.max_balance * 0.4
        cost_b = parent_b.resources.max_balance * 0.4
        
        parent_a.resources.wallet_balance -= cost_a
        parent_b.resources.wallet_balance -= cost_b
        
        # Create merged DNA (crossover from both parents)
        merged_dna = DNAProfile.crossover(parent_a.dna, parent_b.dna)
        merged_dna = self.mutate_dna(merged_dna, mutation_rate=0.05)
        
        # Spawn position (midpoint between parents)
        mid_x = (parent_a.position[0] + parent_b.position[0]) / 2.0
        mid_y = (parent_a.position[1] + parent_b.position[1]) / 2.0
        
        # Calculate merged resources
        combined_balance = parent_a.resources.wallet_balance + parent_b.resources.wallet_balance
        combined_credit = (parent_a.resources.credit_score + parent_b.resources.credit_score) / 2.0
        
        # Merge inventories
        merged_inventory = {}
        for item_type in set(list(parent_a.resources.goods_inventory.keys()) + 
                            list(parent_b.resources.goods_inventory.keys())):
            count_a = parent_a.resources.goods_inventory.get(item_type, 0)
            count_b = parent_b.resources.goods_inventory.get(item_type, 0)
            merged_inventory[item_type] = count_a + count_b
        
        return {
            "result": "MERGER_SUCCESS",
            "merged_dna": merged_dna,
            "merged_pos": [mid_x, mid_y],
            "merged_balance": combined_balance,
            "merged_credit": combined_credit,
            "merged_inventory": merged_inventory,
            "parent_a_id": parent_a.id,
            "parent_b_id": parent_b.id
        }
```

#### **AcquireAction** (Hostile Takeover - NEW)

```python
class AcquireAction(Action):
    """
    Hostile acquisition - absorb struggling dots
    Asymmetric version of merging (one dot absorbs another)
    """
    
    def can_execute(self, acquirer, target):
        """Can acquire if target is weak"""
        # Target must be struggling (low balance OR low credit)
        target_struggling = (
            target.resources.wallet_balance < target.resources.max_balance * 0.3 or
            target.resources.credit_score < 30
        )
        
        # Acquirer must be strong and wealthy
        acquirer_strong = (
            acquirer.resources.wallet_balance >= acquirer.resources.max_balance * 0.7 and
            acquirer.resources.credit_score >= 60
        )
        
        return target_struggling and acquirer_strong
    
    def execute(self, acquirer, target, world_state):
        """Execute hostile takeover"""
        # Cost: 1.5x target's current balance (premium for acquisition)
        acquisition_cost = target.resources.wallet_balance * 1.5
        
        if acquirer.resources.wallet_balance < acquisition_cost:
            return {"result": "INSUFFICIENT_FUNDS"}
        
        # Pay acquisition cost
        acquirer.resources.wallet_balance -= acquisition_cost
        
        # Absorb target's inventory
        for item_type, count in target.resources.goods_inventory.items():
            acquirer.resources.add_to_inventory(item_type, count)
        
        # Gain some DNA points from target (knowledge transfer)
        acquired_knowledge = target.dna.get_allocated_points() * 0.2
        acquirer.dna.earned_dna_points += acquired_knowledge
        
        # Target is removed from simulation
        return {
            "result": "ACQUISITION_SUCCESS",
            "cost": acquisition_cost,
            "acquired_inventory": target.resources.goods_inventory,
            "acquired_knowledge": acquired_knowledge,
            "target_id": target.id
        }
```

---

## 🏪 4. World Objects Transformation

### File: `core/food.py` → `core/resource.py` (or keep as food.py)

#### **Resource Class** (Evolution of Food)

**Key Change:** Resources can be picked up (added to inventory) and then consumed OR sold. This creates economic decision-making.

```python
class Resource:
    """
    Collectible resource in the world
    Can be consumed for survival benefits OR sold for money
    Prices fluctuate based on supply/demand
    """
    
    def __init__(self, resource_id, resource_type, position, quantity=1):
        self.id = resource_id
        self.type = resource_type
        self.position = list(position)
        self.quantity = quantity
        
        # Get properties from resource type definition
        self.properties = RESOURCE_TYPES[resource_type]
        self.base_value = self.properties["base_price"]
        self.demand_multiplier = 1.0  # Market-driven price fluctuation
        self.spawn_time = 0.0
        
        # Visual
        self.color = self.properties["color"]
        self.size = 8 + (quantity * 2)
    
    def get_current_price(self):
        """Calculate current market price (for selling)"""
        return self.base_value * self.demand_multiplier
    
    def get_consume_effect(self):
        """Get benefits from consuming (if consumable)"""
        return self.properties.get("consume_effect", None)
    
    def is_consumable(self):
        """Can this resource be consumed?"""
        return self.properties.get("consume_effect") is not None
    
    def update(self, dt, market_state):
        """Update price based on market conditions"""
        self.spawn_time += dt
        
        # Price fluctuates based on supply/demand
        supply = market_state['total_supply'].get(self.type, 1)
        demand = market_state['total_demand'].get(self.type, 1)
        
        # Calculate supply/demand ratio
        ratio = demand / supply if supply > 0 else 2.0
        
        # Adjust multiplier toward equilibrium
        target_multiplier = min(2.5, max(0.3, ratio))
        self.demand_multiplier += (target_multiplier - self.demand_multiplier) * 0.1 * dt
```

#### **Resource Types & Properties**

```python
# Comprehensive commodity economy tied to dot lifestyle and population dynamics
COMMODITY_TYPES = {
    # ===== FOOD COMMODITIES (survival need, different nutritional values) =====
    "grain": {
        "category": "food",
        "base_price": 10,
        "spawn_rate": 2.5,           # Most common food
        "color": (218, 165, 32),      # Goldenrod
        "consume_effect": {
            "energy": +20,            # Low nutrition
            "health": +2
        },
        "market_dynamic": "stable",  # Steady supply
        "description": "Basic food. Low nutrition, but abundant."
    },
    
    "fruit": {
        "category": "food",
        "base_price": 18,
        "spawn_rate": 1.5,           # Medium spawn
        "color": (255, 99, 71),       # Tomato red
        "consume_effect": {
            "energy": +35,            # Medium nutrition
            "health": +5
        },
        "market_dynamic": "seasonal",  # Fluctuates over time
        "description": "Nutritious food. Good energy, moderate availability."
    },
    
    "meat": {
        "category": "food",
        "base_price": 30,
        "spawn_rate": 0.8,           # Rare spawn
        "color": (139, 69, 19),       # Saddle brown
        "consume_effect": {
            "energy": +50,            # High nutrition
            "health": +10
        },
        "market_dynamic": "scarcity",  # Always in demand, low supply
        "description": "Premium food. High nutrition, rare."
    },
    
    # ===== PRECIOUS METALS (pure value storage) =====
    "silver": {
        "category": "precious_metal",
        "base_price": 40,
        "spawn_rate": 0.6,
        "color": (192, 192, 192),     # Silver
        "consume_effect": None,       # Cannot eat!
        "market_dynamic": "value_store",  # Holds value, low volatility
        "description": "Precious metal. Stable value, good for savings."
    },
    
    "gold": {
        "category": "precious_metal",
        "base_price": 80,
        "spawn_rate": 0.3,            # Rare
        "color": (255, 215, 0),       # Gold
        "consume_effect": None,
        "market_dynamic": "value_store",  # Premium value storage
        "description": "Premium metal. Ultimate value storage."
    },
    
    # ===== LIFESTYLE COMMODITIES (demand scales with population) =====
    "clothing": {
        "category": "lifestyle",
        "base_price": 15,
        "spawn_rate": 1.2,
        "color": (100, 149, 237),     # Cornflower blue
        "consume_effect": None,
        "market_dynamic": "population_driven",
        "demand_formula": "total_dots * 0.5",  # More dots = more demand
        "description": "Lifestyle good. Demand grows with population."
    },
    
    "paper": {
        "category": "lifestyle",
        "base_price": 12,
        "spawn_rate": 1.5,            # Initially high
        "color": (245, 245, 220),     # Beige
        "consume_effect": None,
        "market_dynamic": "recycling",
        "recycling_threshold": 100,    # When total paper > 100, recycling kicks in
        "description": "Paper commodity. Supply cycles through recycling."
    },
    
    # ===== UPGRADE ITEMS (consume for permanent benefits) =====
    "dna_serum": {
        "category": "upgrade",
        "base_price": 100,
        "spawn_rate": 0.1,            # Very rare
        "color": (255, 0, 255),       # Magenta
        "consume_effect": {
            "dna_points": +10          # Expand DNA budget!
        },
        "description": "Consume to gain 10 DNA points"
    },
    
    "memory_chip": {
        "category": "upgrade",
        "base_price": 80,
        "spawn_rate": 0.15,
        "color": (0, 191, 255),       # Deep Sky Blue
        "consume_effect": {
            "memory_slots": +5
        },
        "description": "Consume to expand memory"
    },
    
    "medical_kit": {
        "category": "upgrade",
        "base_price": 60,
        "spawn_rate": 0.2,
        "color": (255, 99, 71),       # Tomato Red
        "consume_effect": {
            "max_health": +20,         # Increases bank size!
            "health": +20
        },
        "description": "Consume to increase max health (bigger wallet)"
    },
    
    "energy_core": {
        "category": "upgrade",
        "base_price": 60,
        "spawn_rate": 0.2,
        "color": (255, 223, 0),       # Golden
        "consume_effect": {
            "max_energy": +20,         # Increases inventory capacity!
            "energy": +20
        },
        "description": "Consume to increase max energy (bigger inventory)"
    }
}
```

#### **Market Dynamics System**

**Each commodity type has unique market behavior tied to simulation state:**

```python
class MarketDynamics:
    """
    Calculates supply/demand for each commodity based on simulation state
    Commodities have different drivers creating realistic market complexity
    """
    
    def update_market_state(self, simulation):
        """Calculate prices based on commodity-specific dynamics"""
        
        # ===== FOOD COMMODITIES (survival-driven demand) =====
        # Demand spikes when dots are hungry
        avg_energy = sum(d.resources.energy for d in simulation.dots) / len(simulation.dots)
        hunger_multiplier = 1.0 + (1.0 - avg_energy / 100) * 2.0
        
        for food_type in ["grain", "fruit", "meat"]:
            base_demand = len(simulation.dots) * 0.3  # Each dot needs ~0.3 food/cycle
            self.demand[food_type] = base_demand * hunger_multiplier
        
        # ===== PRECIOUS METALS (wealth storage, inversely correlated with risk) =====
        # When economy is unstable, dots flee to gold/silver
        market_volatility = self.calculate_price_volatility()
        safe_haven_demand = len(simulation.dots) * market_volatility * 0.2
        
        self.demand["silver"] = safe_haven_demand
        self.demand["gold"] = safe_haven_demand * 1.5  # Gold preferred in crisis
        
        # ===== CLOTHING (population-driven demand) =====
        # More dots = more clothing needed (simple linear relationship)
        population = len(simulation.dots)
        self.demand["clothing"] = population * 0.5
        
        # ===== PAPER (recycling mechanics) =====
        # Complex supply curve with recycling threshold
        total_paper_supply = self.count_commodity_in_world("paper")
        total_trades_this_cycle = simulation.stats.trades_this_generation
        
        # Paper needed for trade documentation
        paper_needed = total_trades_this_cycle * 0.1  # 0.1 paper per trade
        
        if total_paper_supply < 50:
            # Scarcity: High demand, high spawn rate
            self.demand["paper"] = paper_needed * 2.0
            self.spawn_rates["paper"] = 2.0
        elif total_paper_supply > 100:
            # Abundance: Recycling kicks in, demand drops, spawn drops
            recycled_paper = min(paper_needed, total_paper_supply * 0.1)
            self.demand["paper"] = max(0, paper_needed - recycled_paper)
            self.spawn_rates["paper"] = 0.3  # Less new paper needed
        else:
            # Normal state
            self.demand["paper"] = paper_needed
            self.spawn_rates["paper"] = 1.5
        
        # ===== UPGRADE ITEMS (wealth-gated luxury demand) =====
        wealthy_dots = [d for d in simulation.dots if d.resources.wallet > d.resources.max_wallet * 0.7]
        
        self.demand["dna_serum"] = len(wealthy_dots) * 0.8
        self.demand["memory_chip"] = len(wealthy_dots) * 0.6
        self.demand["medical_kit"] = len(wealthy_dots) * 0.4
        self.demand["energy_core"] = len(wealthy_dots) * 0.4
    
    def calculate_price(self, commodity_type):
        """Calculate market price from supply/demand"""
        supply = self.supply[commodity_type]
        demand = self.demand[commodity_type]
        base_price = COMMODITY_TYPES[commodity_type]["base_price"]
        
        if supply == 0:
            return base_price * 3.0  # Extreme scarcity
        
        # Price = base * (demand / supply)
        # Clamped to 0.3x - 3.0x base price
        ratio = demand / supply
        multiplier = min(3.0, max(0.3, ratio))
        
        return base_price * multiplier
```

#### **Commodity Interdependencies**

```python
# Some commodities affect each other
COMMODITY_RELATIONSHIPS = {
    # Food scarcity drives up all food prices (substitution effect)
    "food_scarcity_chain": {
        "trigger": "any_food_supply < critical_threshold",
        "effect": "all_food_prices *= 1.3"
    },
    
    # High gold prices signal economic fear (inverse relationship)
    "gold_fear_indicator": {
        "trigger": "gold_price > base_price * 2.0",
        "effect": "market_volatility increases, demand for necessities spikes"
    },
    
    # Paper recycling creates supply bursts
    "paper_recycling_cycle": {
        "trigger": "total_paper > 100",
        "effect": "spawn_rate drops, price crashes, eventually scarcity returns"
    },
    
    # Population boom drives clothing AND food demand
    "population_pressure": {
        "trigger": "population > previous_gen * 1.5",
        "effect": "clothing and grain demand spike together"
    }
}
```

#### **Trading Post** (NEW World Object)

```python
class TradingPost:
    """
    Fixed location marketplace
    Displays current prices, facilitates dot-to-dot trades
    """
    
    def __init__(self, post_id, position):
        self.id = post_id
        self.position = list(position)
        self.radius = 60  # Trading zone radius
        
        # Market board - current prices
        self.price_board = {good_type: info["base_price"] 
                           for good_type, info in GOOD_TYPES.items()}
        
        # Transaction log
        self.recent_trades = []  # Last 10 trades
        
    def update_prices(self, market_state):
        """Update price board based on market conditions"""
        for good_type in GOOD_TYPES.keys():
            supply = market_state['total_supply'].get(good_type, 0)
            demand = market_state['total_demand'].get(good_type, 0)
            
            base = GOOD_TYPES[good_type]["base_price"]
            
            if supply == 0:
                multiplier = 2.0  # Scarcity
            elif demand == 0:
                multiplier = 0.5  # Surplus
            else:
                multiplier = min(2.0, max(0.5, demand / supply))
            
            self.price_board[good_type] = base * multiplier
    
    def is_in_range(self, position):
        """Check if dot is within trading range"""
        dx = position[0] - self.position[0]
        dy = position[1] - self.position[1]
        distance = math.sqrt(dx*dx + dy*dy)
        return distance <= self.radius
```

---

## 🌍 5. Simulation Logic Transformation

### File: `core/simulation.py`

#### **Economic Ecosystem Dynamics**

```python
class EconomicSimulation:
    """
    Manages the economic ecosystem
    - Market dynamics (supply/demand)
    - Dot lifecycle (spawn, trade, merge, bankrupt)
    - Economic balancing (prevent collapse)
    """
    
    def __init__(self, world_width, world_height):
        # Entities
        self.dots = []
        self.goods = []
        self.trading_posts = []
        
        # Economic state
        self.total_wealth = 0.0
        self.wealth_distribution = []  # Gini coefficient tracking
        self.market_state = {
            'total_supply': {},
            'total_demand': {},
            'price_history': {}
        }
        
        # Sustainability thresholds
        self.MIN_DOTS = 10
        self.MIN_GOODS = 30
        self.MIN_WEALTH_PER_DOT = 20
        self.MAX_GINI_COEFFICIENT = 0.85  # Wealth inequality limit
        
        # Statistics
        self.total_bankruptcies = 0
        self.total_mergers = 0
        self.total_trades = 0
        self.generation = 0
    
    def update(self, dt):
        """Main simulation loop"""
        # 1. Update all dots (economic decisions)
        self.update_dots(dt)
        
        # 2. Update market prices
        self.update_market_state()
        
        # 3. Update goods spawning
        self.update_goods_spawning(dt)
        
        # 4. Process mergers
        self.process_mergers()
        
        # 5. Remove bankrupt dots
        self.process_bankruptcies()
        
        # 6. Check economic sustainability
        self.check_economic_health()
        
        # 7. Update statistics
        self.update_statistics()
    
    def update_market_state(self):
        """Calculate supply/demand for all good types"""
        # Reset market state
        for good_type in GOOD_TYPES.keys():
            self.market_state['total_supply'][good_type] = 0
            self.market_state['total_demand'][good_type] = 0
        
        # Count supply (goods in world + dot inventories)
        for good in self.goods:
            self.market_state['total_supply'][good.type] += good.quantity
        
        for dot in self.dots:
            for good_type, count in dot.resources.goods_inventory.items():
                self.market_state['total_supply'][good_type] += count
        
        # Estimate demand (dots with low inventory + high balance)
        for dot in self.dots:
            inventory_fullness = dot.resources.get_inventory_fullness()
            cash_richness = dot.resources.wallet_balance / dot.resources.max_balance
            
            if inventory_fullness < 0.5 and cash_richness > 0.3:
                # This dot is a buyer
                for good_type in GOOD_TYPES.keys():
                    if good_type not in dot.resources.goods_inventory:
                        self.market_state['total_demand'][good_type] += 1
    
    def check_economic_health(self):
        """Monitor economy and intervene if needed"""
        # Check 1: Minimum viable economy
        if len(self.dots) < self.MIN_DOTS:
            self.inject_new_traders(self.MIN_DOTS - len(self.dots))
        
        # Check 2: Market liquidity
        if len(self.goods) < self.MIN_GOODS:
            self.spawn_goods(self.MIN_GOODS - len(self.goods))
        
        # Check 3: Wealth distribution (Gini coefficient)
        gini = self.calculate_gini_coefficient()
        if gini > self.MAX_GINI_COEFFICIENT:
            # Too much inequality - redistribute via goods spawning
            self.spawn_goods_near_poor_dots(count=20)
            print(f"⚠️ Economic inequality too high (Gini: {gini:.2f}) - Redistributing resources")
        
        # Check 4: Average wealth per dot
        if len(self.dots) > 0:
            avg_wealth = self.total_wealth / len(self.dots)
            if avg_wealth < self.MIN_WEALTH_PER_DOT:
                # Inject capital stimulus
                self.capital_injection(amount=10 * len(self.dots))
    
    def calculate_gini_coefficient(self):
        """Calculate wealth inequality (0 = perfect equality, 1 = perfect inequality)"""
        if len(self.dots) <= 1:
            return 0.0
        
        wealths = sorted([dot.resources.wallet_balance for dot in self.dots])
        n = len(wealths)
        
        cumsum = 0
        for i, wealth in enumerate(wealths):
            cumsum += (2 * (i + 1) - n - 1) * wealth
        
        return cumsum / (n * sum(wealths)) if sum(wealths) > 0 else 0.0
```

#### **Generation Metrics**

```python
class GenerationMetrics:
    """Track economic performance per generation"""
    
    def __init__(self, generation_num):
        self.generation = generation_num
        
        # Population
        self.starting_dots = 0
        self.ending_dots = 0
        
        # Economic indicators
        self.total_wealth_start = 0.0
        self.total_wealth_end = 0.0
        self.avg_wealth_per_dot = 0.0
        self.median_wealth = 0.0
        self.gini_coefficient = 0.0
        
        # Activity metrics
        self.total_trades = 0
        self.total_mergers = 0
        self.total_bankruptcies = 0
        self.trade_volume = 0.0  # Total money exchanged
        
        # Market stats
        self.avg_prices = {}  # Average price per good type
        self.price_volatility = {}  # Price standard deviation
        
        # Strategic distribution
        self.trader_count = 0     # High buy/sell
        self.investor_count = 0   # High hold
        self.merger_count = 0     # High merge ability
```

---

## 🎨 6. Visualization Transformation - Trading Floor Aesthetic

### **🎮 Visual System Upgrade: Sprite-Based Rendering**

**Philosophy:** Transform from simple geometric shapes to **animated sprite characters** in a "Wall Street trading floor" environment. Dots become tiny traders with personality while maintaining simplicity.

**Technical Approach:** Enhance Pygame with sprite sheet rendering (avoid Unity overkill for 2D Python project).

---

### **🎭 Dot Character Design (Sprite-Based)**

#### **Base Character Components**

```
Simple Dot Trader Anatomy:
┌─────────────────┐
│   ●  ●  (eyes)  │  ← Expressive eyes (open/closed states)
│     ▼   (mouth) │  ← Simple expression indicator
│   ──┬── (body)  │  ← Round blob body (keeps "dot" identity)
│    / \  (legs)  │  ← Stick legs for walking animation
│   👋 👋 (hands) │  ← Hold items/show status
└─────────────────┘

Sprite size: 24x32 pixels (small but readable)
```

#### **Animation States (Sprite Sheets)**

```python
DOT_SPRITE_STATES = {
    # MOVEMENT ANIMATIONS
    "idle": {
        "frames": 2,           # Breathing animation
        "fps": 2,
        "description": "Standing still, eyes blink"
    },
    
    "walk_right": {
        "frames": 4,           # Walking cycle
        "fps": 8,
        "description": "Legs alternate, slight bob"
    },
    
    "walk_left": {
        "frames": 4,
        "fps": 8,
        "description": "Mirror of walk_right"
    },
    
    # ACTION ANIMATIONS
    "trading": {
        "frames": 3,           # Hand raises paper, waves it
        "fps": 6,
        "description": "📄 Holds up paper stub/document"
    },
    
    "holding": {
        "frames": 1,           # Static pose
        "fps": 0,
        "description": "🚫 Arms crossed, 'do not enter' sign overhead"
    },
    
    "buying": {
        "frames": 3,           # Hand reaches out, grabs
        "fps": 8,
        "description": "💰 Hand extends, receives item"
    },
    
    "selling": {
        "frames": 3,           # Hand offers item
        "fps": 8,
        "description": "🏷️ Hand holds item out, money floats up"
    },
    
    "eating": {
        "frames": 3,           # Brings food to mouth
        "fps": 6,
        "description": "🍔 Food moves to face, chomp chomp"
    },
    
    "merging": {
        "frames": 5,           # Two dots approach, merge flash
        "fps": 10,
        "description": "✨ Sparkle effect, two become one"
    },
    
    "starving": {
        "frames": 2,           # Weak wobble
        "fps": 3,
        "description": "😵 Dizzy stars, swaying"
    }
}
```

#### **Status Indicators (Overlays)**

```python
DOT_STATUS_OVERLAYS = {
    # WEALTH INDICATORS
    "top_hat": {
        "condition": "wallet > max_wallet * 0.8",
        "sprite": "tophat_16x16.png",
        "offset": (0, -20),        # Above head
        "description": "🎩 Rich dot indicator"
    },
    
    "money_bag": {
        "condition": "wallet > max_wallet * 0.5",
        "sprite": "moneybag_12x12.png",
        "offset": (10, -10),       # Shoulder badge
        "description": "💰 Moderate wealth"
    },
    
    # ACTION INDICATORS
    "paper_stub": {
        "condition": "current_action == 'trading'",
        "sprite": "paper_8x10.png",
        "offset": (8, 0),          # In hand
        "description": "📄 Wants to trade"
    },
    
    "do_not_enter": {
        "condition": "is_holding == True",
        "sprite": "no_entry_12x12.png",
        "offset": (0, -25),        # Above head
        "description": "🚫 Holding/saving mode"
    },
    
    "dollar_sign": {
        "condition": "just_sold_item == True",  # Temporary
        "sprite": "dollar_10x10.png",
        "offset": (0, -15),
        "float_up": True,          # Floats upward
        "duration": 1.0,           # 1 second
        "description": "💵 Sale complete!"
    },
    
    # HEALTH INDICATORS
    "starvation_stars": {
        "condition": "energy < 20",
        "sprite": "dizzy_stars_16x8.png",
        "offset": (0, -22),
        "rotate": True,            # Spin animation
        "description": "⭐ Low energy warning"
    },
    
    "inventory_full": {
        "condition": "inventory_fullness >= 1.0",
        "sprite": "heavy_icon_10x10.png",
        "offset": (-10, -5),
        "description": "📦 Overloaded"
    }
}
```

---

### **🏢 Trading Floor Environment**

#### **World Layout (2D Top-Down View)**

```
┌─────────────────────────────────────────────────────────┐
│                   TRADING FLOOR                         │
│                                                         │
│  🌳    📦                      📦            🌳        │
│        wood                  metal                      │
│                                                         │
│               ┌─────────────────────┐                  │
│        💎     │   MARKET CENTER     │      🍔         │
│        gems   │    ╔═══════════╗    │     food        │
│               │    ║  PRICES   ║    │                 │
│               │    ║ Food: $15 ║    │     📦          │
│  🏛️           │    ║ Wood: $8  ║    │    metal        │
│ Bank          │    ║ Gems: $50 ║    │                 │
│               │    ╚═══════════╝    │          🏛️     │
│               │   (60px radius)     │        Bank     │
│        💊     │                     │                  │
│      medical  └─────────────────────┘                  │
│                                                         │
│  🍔              Dots walk around                💎    │
│ food            Trading with each other          gems  │
│                                                         │
└─────────────────────────────────────────────────────────┘

Floor: Tiled pattern (like checkered floor)
Background: Subtle grid lines (like trading floor)
Lighting: Slight spotlight on market center
```

#### **Market Center (Central Building)**

```python
class MarketCenter:
    """
    Visual centerpiece - Stock exchange building
    Dots gather here to trade at market prices
    """
    
    def __init__(self, position=(600, 400)):
        self.position = position
        self.radius = 60
        
        # Building sprite
        self.sprite = load_sprite("market_center_120x120.png")
        
        # Price board (LED-style display)
        self.price_board = PriceBoard(position=(position[0], position[1] - 80))
        
        # Trading zone circle (golden glow)
        self.zone_glow_alpha = 0.3
        self.zone_color = (255, 215, 0)  # Gold
        
        # Activity indicators
        self.dots_trading_here = []      # Track active traders
        self.trade_particles = []        # Visual effects
    
    def render(self, screen):
        """Draw market center with dynamic elements"""
        # Draw trading zone glow
        draw_circle_alpha(screen, self.zone_color, self.position, 
                         self.radius, self.zone_glow_alpha)
        
        # Draw building sprite
        screen.blit(self.sprite, 
                   (self.position[0] - 60, self.position[1] - 60))
        
        # Draw price board
        self.price_board.render(screen)
        
        # Draw trade particles (sparkles when trades happen)
        for particle in self.trade_particles:
            particle.update()
            particle.render(screen)
```

#### **Price Board (LED Display)**

```python
class PriceBoard:
    """
    Animated LED-style price display
    Shows current market prices with up/down arrows
    """
    
    def __init__(self, position):
        self.position = position
        self.width = 200
        self.height = 100
        
        # Price tracking for trend arrows
        self.price_history = {}  # {resource_type: [prices]}
        
    def render(self, screen):
        """Draw LED-style price board"""
        # Background panel
        panel_rect = pygame.Rect(self.position[0] - self.width//2,
                                self.position[1],
                                self.width, self.height)
        
        # Dark background with border
        pygame.draw.rect(screen, (20, 20, 20), panel_rect)
        pygame.draw.rect(screen, (255, 215, 0), panel_rect, 2)  # Gold border
        
        # Title
        title_font = pygame.font.Font(None, 20)
        title = title_font.render("MARKET PRICES", True, (255, 215, 0))
        screen.blit(title, (self.position[0] - title.get_width()//2,
                           self.position[1] + 5))
        
        # Price list with trend indicators
        y_offset = 30
        price_font = pygame.font.Font(None, 16)
        
        for resource_type, price in self.get_current_prices().items():
            # Determine trend (up/down arrow)
            trend = self.get_price_trend(resource_type)
            
            # Color based on trend
            if trend > 0:
                color = (76, 175, 80)    # Green (rising)
                arrow = "↑"
            elif trend < 0:
                color = (244, 67, 54)    # Red (falling)
                arrow = "↓"
            else:
                color = (255, 193, 7)    # Yellow (stable)
                arrow = "→"
            
            # Render price line
            text = f"{resource_type.upper()}: ${price:.0f} {arrow}"
            price_text = price_font.render(text, True, color)
            screen.blit(price_text, (self.position[0] - 80,
                                    self.position[1] + y_offset))
            
            y_offset += 15
```

---

### **✨ Visual Effects & Particles**

```python
class TradeParticle:
    """
    Sparkle/coin effect when trades happen
    """
    
    def __init__(self, position, particle_type="coin"):
        self.position = list(position)
        self.particle_type = particle_type
        
        if particle_type == "coin":
            self.color = (255, 215, 0)  # Gold
            self.size = 4
            self.velocity = [random.uniform(-1, 1), random.uniform(-3, -1)]
            self.lifetime = 1.0
        elif particle_type == "sparkle":
            self.color = (255, 255, 255)  # White
            self.size = 3
            self.velocity = [0, -0.5]
            self.lifetime = 0.5
        
        self.age = 0
    
    def update(self):
        """Update particle physics"""
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[1] += 0.2  # Gravity
        self.age += 0.016  # ~60fps
        
    def render(self, screen):
        """Draw particle with fade out"""
        alpha = 1.0 - (self.age / self.lifetime)
        if alpha > 0:
            # Draw with alpha (requires surface)
            color = (*self.color, int(alpha * 255))
            pygame.draw.circle(screen, self.color[:3], 
                             (int(self.position[0]), int(self.position[1])), 
                             self.size)
```

---

### **📦 Asset Requirements**

#### **Sprite Sheets Needed**

```
assets/sprites/
├── dots/
│   ├── dot_idle.png           (2 frames, 24x32 each)
│   ├── dot_walk.png           (4 frames, 24x32 each)
│   ├── dot_trading.png        (3 frames, 24x32 each)
│   ├── dot_buying.png         (3 frames, 24x32 each)
│   ├── dot_selling.png        (3 frames, 24x32 each)
│   ├── dot_eating.png         (3 frames, 24x32 each)
│   ├── dot_holding.png        (1 frame, 24x32)
│   ├── dot_merging.png        (5 frames, 24x32 each)
│   └── dot_starving.png       (2 frames, 24x32 each)
│
├── overlays/
│   ├── tophat.png             (16x16)
│   ├── moneybag.png           (12x12)
│   ├── paper_stub.png         (8x10)
│   ├── no_entry_sign.png      (12x12)
│   ├── dollar_sign.png        (10x10)
│   ├── dizzy_stars.png        (16x8)
│   └── heavy_icon.png         (10x10)
│
├── resources/
│   ├── food.png               (16x16)
│   ├── wood.png               (16x16)
│   ├── metal.png              (16x16)
│   ├── gems.png               (16x16)
│   ├── dna_serum.png          (16x16, glowing)
│   ├── memory_chip.png        (16x16, circuit)
│   ├── medical_kit.png        (16x16, red cross)
│   └── energy_core.png        (16x16, golden orb)
│
├── buildings/
│   ├── market_center.png      (120x120)
│   ├── bank.png               (80x80)
│   └── trading_post.png       (60x60)
│
└── ui/
    ├── price_board_bg.png     (200x100)
    └── floor_tile.png         (32x32, repeating)
```

#### **Simple Placeholder Generation**

Since we want to avoid deep character design, we can:
1. **Generate programmatically** (draw circles with stick figures)
2. **Use AI art generators** (DALL-E, Midjourney for simple sprites)
3. **Free sprite libraries** (OpenGameArt, Kenney.nl)
4. **Pixel art tools** (Aseprite, Piskel for quick creation)

---

### **🎨 Rendering System Architecture**

#### **File: `renderers/sprite_renderer.py` (NEW)**

```python
class SpriteRenderer:
    """
    Enhanced renderer with sprite support
    Replaces simple circle drawing with animated sprites
    """
    
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        # Asset management
        self.sprite_sheets = {}
        self.load_all_sprites()
        
        # Animation controller
        self.animation_controller = AnimationController()
        
        # Particle system
        self.particle_system = ParticleSystem()
        
        # Environment
        self.floor_tile = load_sprite("assets/ui/floor_tile.png")
        self.market_center = MarketCenter()
        
    def load_all_sprites(self):
        """Load all sprite sheets into memory"""
        sprite_paths = {
            "dot_idle": "assets/sprites/dots/dot_idle.png",
            "dot_walk": "assets/sprites/dots/dot_walk.png",
            # ... etc
        }
        
        for name, path in sprite_paths.items():
            self.sprite_sheets[name] = SpriteSheet(path)
    
    def render_dot(self, dot):
        """Render dot with appropriate sprite animation"""
        # Determine animation state
        anim_state = self.get_dot_animation_state(dot)
        
        # Get current frame
        sprite = self.animation_controller.get_frame(dot.id, anim_state)
        
        # Apply wealth-based tint
        tinted_sprite = self.apply_wealth_tint(sprite, dot.resources.wallet)
        
        # Draw sprite
        self.screen.blit(tinted_sprite, dot.position)
        
        # Draw status overlays
        self.render_status_overlays(dot)
        
        # Draw debug vision (optional)
        if DEBUG_MODE:
            self.render_vision_cone(dot)
    
    def get_dot_animation_state(self, dot):
        """Determine which animation to play"""
        if dot.current_action == "buy":
            return "buying"
        elif dot.current_action == "sell":
            return "selling"
        elif dot.current_action == "hold":
            return "holding"
        elif dot.current_action == "consume":
            return "eating"
        elif dot.resources.energy < 20:
            return "starving"
        elif dot.velocity[0] != 0 or dot.velocity[1] != 0:
            return "walk_right" if dot.velocity[0] > 0 else "walk_left"
        else:
            return "idle"
```

---

### **HUD Changes (Trading Floor Theme)**

**OLD HUD:**
```
Health: ███████░░░ 70/100
Energy: ████░░░░░░ 40/100
Attacks: 15
Deaths: 8
Generation: 5
```

**NEW HUD (Wall Street Style):**
```
╔══════════════════════════════════════════════════════════════╗
║  💼 DOT AI 3.0 - TRADING FLOOR SIMULATION                   ║
╠══════════════════════════════════════════════════════════════╣
║  Generation: 5  │  Population: 47 traders  │  Time: 02:34   ║
╠══════════════════════════════════════════════════════════════╣
║  💰 Total Market Cap: $4,250                                 ║
║  📊 Avg Wealth: $90.43  │  📈 Gini: 0.42 (Moderate)          ║
║  🏦 Market Activity: 156 trades this session                 ║
╠══════════════════════════════════════════════════════════════╣
║  📈 MARKET PRICES          │  🎩 WEALTHY DOTS: 8             ║
║     Food:  $15  ↑          │  💼 Active Traders: 23          ║
║     Wood:  $8   →          │  🚫 Holding: 12                 ║
║     Metal: $22  ↑          │  😵 Starving: 4                 ║
║     Gems:  $50  ↓          │                                 ║
╚══════════════════════════════════════════════════════════════╝
```

#### **Good/Commodity Visualization**

```python
def render_good(good, screen):
    """Render tradable good with price tag"""
    
    # Draw good as colored square
    size = 10
    rect = pygame.Rect(good.position[0] - size//2, 
                      good.position[1] - size//2, 
                      size, size)
    pygame.draw.rect(screen, good.color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Border
    
    # Draw price label above good
    price = good.get_current_price()
    price_text = f"${price:.0f}"
    price_surface = font_small.render(price_text, True, (255, 255, 255))
    price_bg = pygame.Surface((price_surface.get_width() + 4, 
                              price_surface.get_height() + 2))
    price_bg.fill((0, 0, 0))
    price_bg.set_alpha(180)
    
    screen.blit(price_bg, (good.position[0] - price_surface.get_width()//2, 
                          good.position[1] - 20))
    screen.blit(price_surface, (good.position[0] - price_surface.get_width()//2, 
                               good.position[1] - 20))
```

#### **Trading Post Visualization**

```python
def render_trading_post(post, screen):
    """Render marketplace building"""
    
    # Draw building
    building_rect = pygame.Rect(post.position[0] - 30, 
                               post.position[1] - 30, 
                               60, 60)
    pygame.draw.rect(screen, (101, 67, 33), building_rect)  # Brown building
    pygame.draw.rect(screen, (255, 215, 0), building_rect, 3)  # Gold border
    
    # Draw trading zone radius
    pygame.draw.circle(screen, (255, 215, 0), post.position, post.radius, 1)
    
    # Draw price board
    y_offset = 0
    for good_type, price in post.price_board.items():
        text = f"{good_type.upper()}: ${price:.0f}"
        text_surface = font_tiny.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (post.position[0] - 25, 
                                   post.position[1] - 40 + y_offset))
        y_offset += 12
```

#### **Transaction Visualization**

```python
def render_transaction_effect(buyer, seller, item_type, screen):
    """Show visual effect when trade occurs"""
    
    # Draw line between buyer and seller
    pygame.draw.line(screen, (255, 215, 0), buyer.position, seller.position, 2)
    
    # Draw item icon moving from seller to buyer
    mid_x = (buyer.position[0] + seller.position[0]) / 2
    mid_y = (buyer.position[1] + seller.position[1]) / 2
    
    item_color = GOOD_COLORS[item_type]
    pygame.draw.circle(screen, item_color, (mid_x, mid_y), 6)
    
    # Draw money icon moving from buyer to seller
    # (would animate over several frames)
```

---

## 📊 7. Metrics & Analytics

### File: `core/metrics_logger.py`

#### **Economic Metrics to Track**

```python
class EconomicMetrics:
    """Comprehensive economic tracking"""
    
    # Wealth metrics
    total_wealth_in_economy: float
    average_wealth_per_dot: float
    median_wealth: float
    wealth_std_deviation: float
    gini_coefficient: float  # Inequality measure
    
    # Activity metrics
    trades_per_generation: int
    buy_transactions: int
    sell_transactions: int
    hold_duration_avg: float
    merger_count: int
    acquisition_count: int
    bankruptcy_count: int
    
    # Market metrics
    trade_volume: float  # Total money exchanged
    price_volatility: Dict[str, float]  # Per good type
    avg_profit_per_trade: float
    market_efficiency: float  # How quickly prices stabilize
    
    # Strategic distribution
    dominant_strategy: str  # "trader", "investor", "merger"
    strategy_distribution: Dict[str, int]
    
    # DNA evolution
    avg_buy_power: float
    avg_sell_power: float
    avg_hold_power: float
    avg_merge_ability: float
```

---

## 🚀 Implementation Roadmap

### **Phase 1: Economic Resources Foundation** (Week 1)
**Goal:** Transform core resource system from health/energy to balance/credit

**Tasks:**
1. ✅ Create `core/economic_resources.py`
   - Implement wallet balance system
   - Implement credit score system
   - Implement inventory system
   - Implement bankruptcy mechanics

2. ✅ Update `core/dna.py` with economic genes
   - Rename existing genes (attack→buy, defend→hold, etc.)
   - Add new genes (sell_power, negotiate)
   - Update gene descriptions

3. ✅ Modify `core/dot.py` to use EconomicResources
   - Replace Resources with EconomicResources
   - Update update() loop for economic costs
   - Update death check for bankruptcy

**Deliverable:** Dots have wallets, credit scores, and can go bankrupt

---

### **Phase 2: Market & Goods System** (Week 2)
**Goal:** Transform food into tradable goods with dynamic pricing

**Tasks:**
1. ✅ Create `core/goods.py` (rename from food.py)
   - Implement Good class with types
   - Add dynamic pricing system
   - Create market state tracking

2. ✅ Create `core/trading_post.py`
   - Implement TradingPost class
   - Add price boards
   - Create trading zones

3. ✅ Update `core/simulation.py`
   - Replace food spawning with goods spawning
   - Implement market state updates
   - Add supply/demand calculations

**Deliverable:** Goods spawn with prices that fluctuate based on supply/demand

---

### **Phase 3: Economic Actions** (Week 3)
**Goal:** Implement buy, sell, hold, and merge actions

**Tasks:**
1. ✅ Transform `core/actions.py`
   - Implement BuyAction (replace AttackAction)
   - Implement SellAction (new)
   - Implement HoldAction (replace DefendAction)
   - Implement MergeAction (replace ReplicateAction)
   - Implement AcquireAction (new - hostile takeover)

2. ✅ Update `core/brain.py` utility calculations
   - Create calculate_buy_utility()
   - Create calculate_sell_utility()
   - Create calculate_hold_utility()
   - Create calculate_merge_utility()

3. ✅ Update `core/dot.py` decision making
   - Wire new actions to utility system
   - Update execute_action() for economic actions
   - Handle merger results (parent dissolution)

**Deliverable:** Dots can buy, sell, hold, and merge strategically

---

### **Phase 4: Simulation & Balancing** (Week 4)
**Goal:** Economic ecosystem with sustainability checks

**Tasks:**
1. ✅ Update `core/simulation.py`
   - Implement economic health checks
   - Add Gini coefficient calculation
   - Implement auto-balancing (capital injection, goods spawning)
   - Process mergers (remove parents, spawn offspring)
   - Process bankruptcies (liquidate assets)

2. ✅ Create economic metrics tracking
   - Update `core/metrics_logger.py`
   - Track wealth distribution
   - Track trade volumes
   - Track market efficiency

3. ✅ Balance economic parameters
   - Tune operational costs
   - Adjust good spawn rates
   - Calibrate interest rates
   - Test merger mechanics

**Deliverable:** Self-sustaining economic ecosystem with intervention systems

---

### **Phase 5: Visualization & Polish** (Week 5)
**Goal:** Trading floor aesthetic with sprite-based rendering

**Tasks:**
1. ✅ Create sprite system infrastructure
   - Implement `SpriteRenderer` class
   - Create `AnimationController` for sprite animations
   - Build `SpriteSheet` loader

2. ✅ Design/generate sprite assets
   - Create simple dot character sprites (eyes, hands, feet)
   - Design 8 animation states (idle, walk, trading, etc.)
   - Create status overlay icons (top hat, paper stub, etc.)
   - Design market center building sprite
   - Create resource item sprites

3. ✅ Implement trading floor environment
   - Render checkered floor background
   - Place market center building (central hub)
   - Add price board LED display
   - Implement particle effects (coins, sparkles)

4. ✅ Add status indicators
   - Top hats for wealthy dots
   - Paper stubs when wanting to trade
   - "Do not enter" signs when holding
   - Starvation stars for low energy
   - Inventory full icon

5. ✅ Update HUD to Wall Street theme
   - Box-style layout with borders
   - Market ticker with trend arrows
   - Wealth distribution stats
   - Activity indicators

**Deliverable:** Beautiful trading floor simulation with animated sprite characters

**Technical Notes:**
- Stay with Pygame (no Unity needed)
- Use simple procedural sprites if needed (circles + stick figures)
- Focus on clarity over artistic detail
- Maintain 60fps performance with 50+ animated dots

---

### **Phase 6: Testing & Experiments** (Week 6)
**Goal:** Validate emergent economic behaviors

**Experiments:**
1. **Trader vs Investor Evolution**
   - Do high buy/sell dots dominate early game?
   - Do high hold dots win long-term?

2. **Merger Strategies**
   - Do mergers create monopolies?
   - Is there optimal merge timing?

3. **Market Dynamics**
   - Do prices stabilize or oscillate?
   - How does scarcity affect evolution?

4. **Wealth Distribution**
   - Does inequality increase over time?
   - Can wealth redistribution prevent collapse?

**Deliverable:** Documented findings and balanced parameters

---

## 🎓 Expected Emergent Behaviors

### **Economic-Survival Niches**

**The hybrid system creates more complex niches than pure combat or pure economics!**

1. **Subsistence Survivors** (Low economic genes, high survival)
   - Eat all food immediately (never sell)
   - Live hand-to-mouth, always near starvation
   - Can't afford upgrades, stuck at basic DNA
   - **Evolutionary dead-end?** OR stable minimum strategy?

2. **Hustler Traders** (High buy/sell, moderate survival)
   - Risk starvation to sell food for profit
   - Flip materials rapidly
   - Boom-bust cycle: rich then starve, repeat
   - **High-risk, high-reward strategy**

3. **Conservative Investors** (High hold, high food gathering)
   - Stockpile food for safety
   - Sell excess food for steady income
   - Earn interest, buy upgrades slowly
   - **Stable long-term growth**

4. **Upgrade Rushers** (High gathering, strategic selling)
   - Prioritize DNA serum and memory chips
   - Sacrifice short-term survival for long-term power
   - Gamble on reaching "escape velocity" before starving
   - **Investment in self vs immediate needs**

5. **Resource Magnates** (High inventory, strategic hoarding)
   - Hoard food when scarce (prices spike)
   - Sell during famines at premium prices
   - **Market manipulation through scarcity**
   - Ethical question: profit from others' starvation?

6. **Merger Moguls** (High merge, balanced resources)
   - Build wealth to attract merger partners
   - Combine DNA pools for stronger offspring
   - **Conglomerate formation**

7. **Upgrade Addicts** (Luxury consumers)
   - Focus entirely on buying upgrade items
   - Expand DNA budget beyond 100+ points
   - Become super-dots but risk bankruptcy
   - **Power scaling strategy**

### **Strategic Emergent Questions**

**When does eating food become less valuable than selling it?**
- If energy > 70% AND food price > 2x base → Sell wins
- If energy < 30% → Eat always wins
- **Middle zone = interesting decisions**

**Is there an "upgrade tipping point"?**
- At what DNA level do gathering abilities improve enough to justify the investment?
- Does 120 DNA points = 20% better gathering = ROI positive?
- **Economic calculus emerges naturally**

**Do market crashes kill or create opportunities?**
- Food shortage → Prices spike → Hoarders profit
- But also → Many dots starve → Population crash → Market collapse
- **Boom-bust economic cycles**

**Will wealth concentration lead to extinction?**
- If one dot hoards all food → Others starve → Buyer disappears → Hoarder has no market
- **Tragedy of the commons encoded in simulation**

### **Market Cycles**

1. **Boom Phase**
   - High trade volume
   - Rising prices
   - Many mergers

2. **Bust Phase**
   - Low liquidity
   - Bankruptcies spike
   - Price crashes

3. **Recovery Phase**
   - Capital injection
   - Goods respawn
   - Cautious trading resumes

---

## 🔬 Research Questions

### **Commodity Market Dynamics**

1. **Food Substitution Effects**
   - Will dots learn to eat grain when meat is expensive?
   - Do nutritional differences create quality tiers?
   - Does meat hoarding create artificial famines?

2. **Paper Recycling Cycles**
   - Will paper markets exhibit boom-bust oscillations?
   - What's the period of the recycling cycle?
   - Can dots exploit the cycle for profit?

3. **Population-Driven Demand**
   - Does clothing demand stabilize population growth?
   - Do high clothing prices suppress reproduction (mergers)?
   - Is there a population equilibrium point?

4. **Precious Metals as Crisis Hedge**
   - Do gold prices spike during food shortages?
   - Will dots flee to gold during market volatility?
   - Does gold hoarding accelerate crashes?

### **Economic Strategy Evolution**

5. **Gathering vs Trading Strategies**
   - Is it better to gather (free) or buy (fast)?
   - Do high gather_speed genes dominate early game?
   - Do traders outcompete gatherers in mature economies?

6. **Hoarding vs Flipping**
   - Does hoarding create profitable scarcity?
   - Or does inventory space limit hoarder effectiveness?
   - Will market manipulators evolve naturally?

7. **Upgrade Addiction**
   - Can dots reach "escape velocity" with DNA upgrades?
   - What's the optimal upgrade timing (early vs late)?
   - Do upgraded dots dominate or starve trying?

### **Market Collapse Scenarios**

8. **Starvation Cascades**
   - If food supply drops, do bankruptcies spike?
   - Does population crash restore food availability?
   - Can the market self-correct from near-extinction?

9. **Deflationary Spirals**
   - If everyone hoards, does demand collapse?
   - Do falling prices trigger bankruptcy cascades?
   - Is there a minimum viable economy size?

10. **Wealth Inequality**
    - What Gini coefficient causes market breakdown?
    - Do monopolists kill their own markets?
    - Can wealth redistribution prevent collapse?

### **Real-World Economic Parallels**

11. **Can we model inflation/deflation?**
    - Does money supply (wallet totals) affect prices?
    - Do upgrade purchases act as money sinks?

12. **Will supply chain disruptions emerge?**
    - If paper becomes scarce, do trades slow down?
    - Do commodity shortages cascade to other goods?

13. **Do speculative bubbles form?**
    - Will dots overvalue gold during crises?
    - Can bubble bursts trigger economic downturns?

---

## 📝 Technical Notes

### **DNA Compatibility**
- Keep DNAProfile.crossover() system (unchanged)
- Mutation system stays the same
- Budget system identical to 2.0

### **Rendering Compatibility**
- Pygame renderer architecture unchanged
- Replace sprite rendering logic only
- HUD system adapts, not rewrites

### **Metrics Compatibility**
- MetricsLogger structure stays similar
- Replace combat metrics with economic metrics
- Generation tracking identical

### **Save/Load System**
- Simulation saves should work similarly
- Add economic state to serialization
- Maintain backwards compatibility where possible

---

## 🎯 Success Criteria

**Minimum Viable Product (MVP):**
- [ ] Dots use wallet + energy (hybrid survival-economic resources)
- [ ] 3 food types spawn with different nutrition values
- [ ] Commodities spawn with dynamic prices (supply/demand)
- [ ] Dots can gather (free) and buy/sell (paid) commodities
- [ ] Food: eat or sell decision
- [ ] Mergers create offspring with combined resources
- [ ] Bankruptcy removes dots from simulation
- [ ] Basic economic HUD displays

**Full Release:**
- [ ] All commodity types functional (food, metals, lifestyle, upgrades)
- [ ] Market dynamics create realistic price fluctuations
- [ ] Paper recycling mechanics working
- [ ] Population-driven clothing demand
- [ ] Economic niches emerge (gatherers vs traders vs hoarders)
- [ ] Wealth inequality tracked and balanced
- [ ] Trading floor sprite-based visualization
- [ ] At least 5 documented emergent behaviors

**Stretch Goals:**
- [ ] 10+ commodity types (industries: tech, energy, housing)
- [ ] Dot-to-dot direct trading (not just market center)
- [ ] Commodity derivatives (futures/options) - Phase 2 feature
- [ ] Loan system (dots can borrow from "bank")
- [ ] Economic disasters (supply shocks, demand crashes)
- [ ] Multi-market simulation (competing trading floors)

---

## 📚 Documentation Needed

1. **DOT_AI_3.0_README.md**
   - Explain commodity-focused economic simulation
   - Trading floor metaphor
   - Multiple food types and market dynamics
   - New experiment ideas (hoarding, market manipulation, upgrade rushes)

2. **COMMODITY_MECHANICS.md**
   - Detailed explanation of each commodity type
   - Market dynamics formulas
   - Recycling mechanics (paper)
   - Population-driven demand (clothing)
   - Economic balance formulas

3. **TRADING_STRATEGIES.md**
   - Gatherer vs Trader strategies
   - Hoarding for profit
   - Market timing (buy low, sell high)
   - Upgrade investment timing
   - Food nutrition optimization

4. **MIGRATION_GUIDE.md**
   - How to convert 2.0 saves to 3.0
   - DNA translation guide (attack→buy_power, defend→sell_power)
   - Metric comparison table

5. **PHASE_X_COMPLETE.md** (for each phase)
   - Implementation notes
   - Bugs fixed
   - Parameter tuning decisions

---

## 🎯 Key Design Principles (Summary)

### **What Makes Dot AI 3.0 Unique**

1. **No Physical Combat** - All conflict is economic
   - Compete through market timing, not fighting
   - Win by accumulating wealth, not killing enemies
   - "Fight with the pen, not the sword"

2. **Dual-Purpose Resources** - Eat or sell dilemma
   - Food restores energy OR generates money
   - Creates strategic tension every decision
   - Poor dots must eat, rich dots can trade

3. **Realistic Market Dynamics** - Tied to simulation state
   - Food demand driven by hunger (survival need)
   - Clothing demand driven by population (lifestyle need)
   - Gold demand driven by fear (safe haven)
   - Paper supply cycles through recycling (complex dynamics)

4. **Progressive Upgrades** - Economic advancement
   - DNA serums expand ability points
   - Medical kits increase wallet capacity
   - Energy cores increase inventory capacity
   - Creates vertical progression (not just horizontal)

5. **Sprite-Based Trading Floor** - Visual storytelling
   - Dots with eyes, hands, feet show personality
   - Status indicators (top hats, paper stubs, dizzy stars)
   - Central market center building
   - Wall Street aesthetic HUD

### **Evolution from 2.0 → 3.0**

| **Aspect** | **Dot AI 2.0** | **Dot AI 3.0** |
|------------|----------------|----------------|
| **Survival** | Combat & food gathering | Food purchasing & market trading |
| **Competition** | Attack/defend actions | Buy/sell/hoard strategies |
| **Death** | Starvation or combat damage | Starvation or bankruptcy |
| **Reproduction** | Sexual/asexual with energy cost | Mergers with capital requirements |
| **Resources** | Energy + Health | Energy + Health + Wallet + Inventory |
| **Complexity** | DNA points from eating | DNA points from upgrade purchases |
| **Visualization** | Simple circles | Animated sprites with status overlays |
| **Emergent Behavior** | Predator/prey dynamics | Market manipulation & boom/bust cycles |

---

**END OF PLAN**

This plan maintains the core strengths of Dot AI 2.0 (DNA evolution, utility-based AI, emergent complexity) while completely transforming the survival mechanics into a **commodity-focused economic simulation**. The AI principles remain unchanged - only the inputs, actions, and objectives differ. Dots now compete through **economic warfare** rather than physical combat, creating a unique "Wall Street meets evolution simulator" experience.
