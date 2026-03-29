"""
Market System - DOT AI 3.0
Handles commodity spawning, pricing, and scarcity-based economics

Key Concepts:
- Finite resources (no respawn)
- Realistic metric ton pricing
- Scarcity-driven price increases
- 5-tier metal hierarchy (scrap → iron → bronze → silver → gold)
"""

import random
import math


class Commodity:
    """
    Represents a tradable commodity in the world
    
    Can be:
    - Gathered from world (spawned at start, finite quantity)
    - Bought from market center
    - Sold to market center
    - Consumed (food only)
    - Stored in inventory
    """
    
    def __init__(self, commodity_type, position, quantity=1):
        self.type = commodity_type
        self.position = list(position)  # [x, y]
        self.quantity = quantity
        self.gathered = False  # Has someone picked this up?
    
    def serialize(self):
        return {
            "type": self.type,
            "position": self.position,
            "quantity": self.quantity,
            "gathered": self.gathered
        }


class CommodityType:
    """
    Definition of a commodity type (what it is, base value, total world supply)
    """
    
    def __init__(self, name, base_price, total_supply, can_consume=False, energy_value=0):
        self.name = name
        self.base_price = base_price  # Base price per unit
        self.total_supply = total_supply  # Total units in world (finite!)
        self.remaining_supply = total_supply  # Current ungathered supply
        self.can_consume = can_consume  # Can dots eat this?
        self.energy_value = energy_value  # Energy gained if consumed
        
        # Price tracking
        self.current_price = base_price
        self.price_history = [base_price]
    
    def update_price(self):
        """
        Update price based on scarcity.
        As supply depletes, price increases exponentially.
        
        Formula: price = base_price × (total_supply / remaining_supply)^2
        
        Example: Gold
        - Start: 3 remaining → price = $60,000 × (3/3)^2 = $60,000
        - Mid: 2 remaining → price = $60,000 × (3/2)^2 = $135,000
        - End: 1 remaining → price = $60,000 × (3/1)^2 = $540,000
        """
        if self.remaining_supply <= 0:
            self.current_price = self.base_price * 100  # Extinct commodity is priceless
        else:
            scarcity_multiplier = (self.total_supply / self.remaining_supply) ** 2
            self.current_price = self.base_price * scarcity_multiplier
        
        self.price_history.append(self.current_price)
    
    def gather_item(self, quantity=1):
        """
        Remove items from world supply (someone gathered them).
        Returns: actual quantity gathered (may be less if insufficient supply)
        """
        actual_gathered = min(quantity, self.remaining_supply)
        self.remaining_supply -= actual_gathered
        self.update_price()
        return actual_gathered
    
    def serialize(self):
        return {
            "name": self.name,
            "base_price": self.base_price,
            "total_supply": self.total_supply,
            "remaining_supply": self.remaining_supply,
            "current_price": self.current_price,
            "can_consume": self.can_consume,
            "energy_value": self.energy_value,
            "scarcity_pct": (1 - self.remaining_supply / self.total_supply) * 100
        }


class Market:
    """
    Central market system for the simulation.
    
    Manages:
    - Commodity type definitions
    - Global supply tracking
    - Price calculations
    - World commodity spawning
    """
    
    def __init__(self, world_width=1200, world_height=800):
        self.world_width = world_width
        self.world_height = world_height
        
        # Commodity type definitions (based on realistic metric ton pricing)
        self.commodity_types = {}
        self._initialize_commodity_types()
        
        # World commodities (physical items in world that can be gathered)
        self.world_commodities = []
    
    def _initialize_commodity_types(self):
        """
        Define all commodity types with realistic pricing.
        
        Prices scaled from real-world metric ton values:
        - Scrap: $200/ton → $0.20 base
        - Cast Iron: $500/ton → $0.50 base
        - Bronze: $8,000/ton → $8.00 base
        - Silver: $700,000/ton → $700 base
        - Gold: $60,000,000/ton → $60,000 base
        
        Supply scaled to create scarcity dynamics.
        """
        
        # FOOD (consumable, energy source)
        self.commodity_types["food_grain"] = CommodityType(
            name="food_grain",
            base_price=1.0,
            total_supply=100,  # Moderate supply
            can_consume=True,
            energy_value=30.0  # Restores 30 energy
        )
        
        self.commodity_types["food_meat"] = CommodityType(
            name="food_meat",
            base_price=3.0,
            total_supply=40,  # Scarcer than grain
            can_consume=True,
            energy_value=50.0  # Restores 50 energy (better than grain)
        )
        
        # METALS (trade goods, 5-tier hierarchy)
        
        # Tier 1: Scrap (abundant, low value)
        self.commodity_types["scrap"] = CommodityType(
            name="scrap",
            base_price=0.20,
            total_supply=200,  # Most abundant
            can_consume=False,
            energy_value=0
        )
        
        # Tier 2: Iron (common, moderate value)
        self.commodity_types["iron"] = CommodityType(
            name="iron",
            base_price=0.50,
            total_supply=80,
            can_consume=False,
            energy_value=0
        )
        
        # Tier 3: Bronze (uncommon, good value)
        self.commodity_types["bronze"] = CommodityType(
            name="bronze",
            base_price=8.0,
            total_supply=30,
            can_consume=False,
            energy_value=0
        )
        
        # Tier 4: Silver (rare, high value)
        self.commodity_types["silver"] = CommodityType(
            name="silver",
            base_price=700.0,
            total_supply=10,
            can_consume=False,
            energy_value=0
        )
        
        # Tier 5: Gold (ultra-rare, extreme value)
        self.commodity_types["gold"] = CommodityType(
            name="gold",
            base_price=60000.0,
            total_supply=3,  # Only 3 in entire world!
            can_consume=False,
            energy_value=0
        )
    
    def spawn_commodities(self, multiplier=1.0):
        """
        Spawn all commodities in the world at simulation start.
        
        Args:
            multiplier: Scale commodity quantities (default 1.0, use 0.5 for scarcity testing)
        
        Distribution:
        - Food: Scattered evenly
        - Scrap/Iron: Common, scattered
        - Bronze: Clustered (resource deposits)
        - Silver/Gold: Very rare, isolated locations
        """
        self.world_commodities = []
        
        for commodity_name, commodity_type in self.commodity_types.items():
            # Apply multiplier to total supply (but keep at least 1)
            total = max(1, int(commodity_type.total_supply * multiplier))
            
            # Spawn each unit
            for i in range(total):
                # Random position in world
                x = random.randint(50, self.world_width - 50)
                y = random.randint(50, self.world_height - 50)
                
                # Create commodity instance
                commodity = Commodity(commodity_name, [x, y], quantity=1)
                self.world_commodities.append(commodity)
        
        print(f"[MARKET] Spawned {len(self.world_commodities)} commodities (multiplier: {multiplier}x)")
        for name, ctype in self.commodity_types.items():
            actual_spawned = int(ctype.total_supply * multiplier)
            print(f"  {name}: {actual_spawned} units @ ${ctype.base_price:.2f} each")
    
    def get_price(self, commodity_name):
        """Get current market price for commodity"""
        if commodity_name in self.commodity_types:
            return self.commodity_types[commodity_name].current_price
        return 0.0
    
    def get_supply(self, commodity_name):
        """Get remaining supply for commodity"""
        if commodity_name in self.commodity_types:
            return self.commodity_types[commodity_name].remaining_supply
        return 0
    
    def can_consume(self, commodity_name):
        """Check if commodity is consumable (food)"""
        if commodity_name in self.commodity_types:
            return self.commodity_types[commodity_name].can_consume
        return False
    
    def get_energy_value(self, commodity_name):
        """Get energy value if consumed"""
        if commodity_name in self.commodity_types:
            return self.commodity_types[commodity_name].energy_value
        return 0.0
    
    def buy_from_market(self, commodity_name, quantity=1):
        """
        Buy commodity from market (not from world, from abstract market center).
        
        This represents buying from other traders/market makers.
        Price is current market price.
        
        Returns: (success: bool, total_cost: float)
        """
        if commodity_name not in self.commodity_types:
            return False, 0.0
        
        commodity_type = self.commodity_types[commodity_name]
        
        # Check supply
        if commodity_type.remaining_supply < quantity:
            return False, 0.0
        
        # Calculate cost
        total_cost = commodity_type.current_price * quantity
        
        # Deduct from supply
        commodity_type.gather_item(quantity)
        
        return True, total_cost
    
    def sell_to_market(self, commodity_name, quantity=1):
        """
        Sell commodity to market (abstract market center).
        
        Returns: (success: bool, total_payment: float)
        """
        if commodity_name not in self.commodity_types:
            return False, 0.0
        
        commodity_type = self.commodity_types[commodity_name]
        
        # Calculate payment (current market price)
        total_payment = commodity_type.current_price * quantity
        
        # Add back to supply (sold items re-enter market)
        commodity_type.remaining_supply += quantity
        commodity_type.update_price()
        
        return True, total_payment
    
    def find_nearest_commodity(self, position, commodity_type=None, max_distance=None):
        """
        Find nearest ungathered commodity to position.
        
        Args:
            position: [x, y]
            commodity_type: Filter by type (e.g., "food_grain"), or None for any
            max_distance: Maximum search radius, or None for unlimited
        
        Returns: Commodity object or None
        """
        nearest = None
        nearest_distance = float('inf')
        
        for commodity in self.world_commodities:
            # Skip gathered commodities
            if commodity.gathered:
                continue
            
            # Filter by type
            if commodity_type and commodity.type != commodity_type:
                continue
            
            # Calculate distance
            dx = commodity.position[0] - position[0]
            dy = commodity.position[1] - position[1]
            distance = math.sqrt(dx**2 + dy**2)
            
            # Check max distance
            if max_distance and distance > max_distance:
                continue
            
            # Update nearest
            if distance < nearest_distance:
                nearest = commodity
                nearest_distance = distance
        
        return nearest
    
    def gather_commodity(self, commodity):
        """
        Mark commodity as gathered (remove from world).
        
        Args:
            commodity: Commodity object to gather
        
        Returns: (commodity_type: str, quantity: int)
        """
        if commodity.gathered:
            return None, 0
        
        commodity.gathered = True
        
        # Deduct from global supply
        if commodity.type in self.commodity_types:
            self.commodity_types[commodity.type].gather_item(commodity.quantity)
        
        return commodity.type, commodity.quantity
    
    def get_market_snapshot(self):
        """
        Get current market state (for analytics/display).
        
        Returns: dict with all commodity data
        """
        snapshot = {
            "commodities": {},
            "total_value": 0.0,
            "scarcest": None,
            "most_expensive": None
        }
        
        for name, ctype in self.commodity_types.items():
            data = ctype.serialize()
            snapshot["commodities"][name] = data
            
            # Track total market value
            snapshot["total_value"] += ctype.current_price * ctype.remaining_supply
            
            # Track scarcest (lowest remaining %)
            scarcity_pct = data["scarcity_pct"]
            if snapshot["scarcest"] is None or scarcity_pct > snapshot["scarcest"]["scarcity_pct"]:
                snapshot["scarcest"] = {"name": name, "scarcity_pct": scarcity_pct}
            
            # Track most expensive
            if snapshot["most_expensive"] is None or ctype.current_price > snapshot["most_expensive"]["price"]:
                snapshot["most_expensive"] = {"name": name, "price": ctype.current_price}
        
        return snapshot
    
    def get_ungathered_count(self):
        """Count how many commodities remain in world"""
        return sum(1 for c in self.world_commodities if not c.gathered)
    
    def serialize(self):
        """Export market state"""
        return {
            "commodity_types": {name: ctype.serialize() for name, ctype in self.commodity_types.items()},
            "world_commodities_total": len(self.world_commodities),
            "world_commodities_ungathered": self.get_ungathered_count(),
            "market_snapshot": self.get_market_snapshot()
        }
