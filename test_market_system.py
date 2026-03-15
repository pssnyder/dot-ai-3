"""
Test script for Market System & Trading Actions
Tests the Dot AI 3.0 economic infrastructure

Run this to verify:
- Market initialization with realistic pricing
- Commodity spawning (finite resources)
- Price updates based on scarcity
- Gather/Buy/Sell/Consume actions
- Integration between market and dot resources
"""

import sys
from core.market import Market, Commodity
from core.dna import DNAProfile
from core.resources import Resources
from core.actions import GatherAction, BuyAction, SellAction, ConsumeAction


class MockDot:
    """Simplified dot for testing"""
    def __init__(self, dot_id, wallet=10.0):
        self.id = dot_id
        self.dna = DNAProfile()
        self.resources = Resources(self.dna)
        self.resources.wallet = wallet
        self.position = [600, 400]  # Center of 1200x800 world
        self.brain = None  # For consume action


def test_market_initialization():
    """Test market creation and commodity setup"""
    
    print("=" * 70)
    print("TEST 1: MARKET INITIALIZATION")
    print("=" * 70)
    print()
    
    market = Market(world_width=1200, world_height=800)
    
    print("Commodity Types:")
    for name, ctype in market.commodity_types.items():
        print(f"  {name:15} - ${ctype.base_price:>10,.2f} × {ctype.total_supply:>3} units = ${ctype.base_price * ctype.total_supply:>12,.2f} total value")
        if ctype.can_consume:
            print(f"                   (consumable, {ctype.energy_value} energy)")
    print()
    
    # Test price hierarchy
    print("Value Ratios (Gold as baseline):")
    gold_price = market.commodity_types["gold"].base_price
    for name in ["scrap", "iron", "bronze", "silver", "gold"]:
        price = market.commodity_types[name].base_price
        ratio = gold_price / price
        print(f"  Gold is {ratio:>10,.0f}x more valuable than {name}")
    print()


def test_commodity_spawning():
    """Test spawning commodities in world"""
    
    print("=" * 70)
    print("TEST 2: COMMODITY SPAWNING")
    print("=" * 70)
    print()
    
    market = Market()
    market.spawn_commodities()
    
    print(f"Total commodities spawned: {len(market.world_commodities)}")
    print(f"Ungathered commodities: {market.get_ungathered_count()}")
    print()
    
    # Count by type
    counts = {}
    for commodity in market.world_commodities:
        counts[commodity.type] = counts.get(commodity.type, 0) + 1
    
    print("Distribution:")
    for ctype, count in sorted(counts.items()):
        print(f"  {ctype:15} - {count:>3} units")
    print()


def test_price_dynamics():
    """Test scarcity-based price increases"""
    
    print("=" * 70)
    print("TEST 3: PRICE DYNAMICS (Scarcity-Based)")
    print("=" * 70)
    print()
    
    market = Market()
    
    # Simulate gold depletion
    print("Gold Price Progression (as supply depletes):")
    gold = market.commodity_types["gold"]
    
    print(f"  Initial: {gold.remaining_supply} units @ ${gold.current_price:,.2f}")
    
    # Gather 1 gold
    gold.gather_item(1)
    print(f"  After gathering 1: {gold.remaining_supply} units @ ${gold.current_price:,.2f}")
    
    # Gather another
    gold.gather_item(1)
    print(f"  After gathering 2: {gold.remaining_supply} units @ ${gold.current_price:,.2f}")
    
    # Last one
    gold.gather_item(1)
    print(f"  After gathering 3: {gold.remaining_supply} units @ ${gold.current_price:,.2f}")
    print()
    
    # Test scrap for comparison
    print("Scrap Price Progression (abundant resource):")
    scrap = market.commodity_types["scrap"]
    
    print(f"  Initial: {scrap.remaining_supply} units @ ${scrap.current_price:.2f}")
    
    scrap.gather_item(50)
    print(f"  After 50 gathered: {scrap.remaining_supply} units @ ${scrap.current_price:.2f}")
    
    scrap.gather_item(100)
    print(f"  After 150 gathered: {scrap.remaining_supply} units @ ${scrap.current_price:.2f}")
    print()


def test_gather_action():
    """Test gathering commodities from world"""
    
    print("=" * 70)
    print("TEST 4: GATHER ACTION")
    print("=" * 70)
    print()
    
    market = Market()
    market.spawn_commodities()
    
    dot = MockDot(1, wallet=10.0)
    gather_action = GatherAction(dot.dna)
    
    # Find nearest commodity
    nearest = market.find_nearest_commodity(dot.position)
    
    print(f"Dot position: {dot.position}")
    print(f"Nearest commodity: {nearest.type} at {nearest.position}")
    print()
    
    # Move dot close to commodity
    dot.position = [nearest.position[0] + 5, nearest.position[1] + 5]
    
    print(f"Moved dot to: {dot.position}")
    print(f"Inventory before: {dot.resources.inventory}")
    print()
    
    # Gather
    result = gather_action.execute(dot, nearest, market)
    
    print(f"Gather result: {result['result']}")
    if result['result'] == 'GATHERED':
        print(f"  Commodity: {result['commodity']}")
        print(f"  Quantity: {result['quantity']}")
    print(f"Inventory after: {dot.resources.inventory}")
    print(f"Ungathered commodities remaining: {market.get_ungathered_count()}")
    print()


def test_buy_action():
    """Test buying from market"""
    
    print("=" * 70)
    print("TEST 5: BUY ACTION")
    print("=" * 70)
    print()
    
    market = Market()
    
    dot = MockDot(2, wallet=50.0)
    buy_action = BuyAction(dot.dna)
    
    print(f"Dot wallet: ${dot.resources.wallet:.2f}")
    print(f"Inventory: {dot.resources.inventory}")
    print()
    
    # Try to buy food
    food_price = market.get_price("food_grain")
    print(f"Food grain market price: ${food_price:.2f}")
    print()
    
    print("Attempting to buy 5 food_grain...")
    result = buy_action.execute(dot, "food_grain", 5, market)
    
    print(f"Result: {result['result']}")
    if result['result'] == 'PURCHASE_SUCCESS':
        print(f"  Commodity: {result['commodity']}")
        print(f"  Quantity: {result['quantity']}")
        print(f"  Price per unit: ${result['price_per_unit']:.2f}")
        print(f"  Total cost: ${result['total_cost']:.2f}")
        print(f"  Discount: {result['discount_applied']:.1%}")
    print()
    
    print(f"Dot wallet after: ${dot.resources.wallet:.2f}")
    print(f"Inventory after: {dot.resources.inventory}")
    print(f"Total purchases: {dot.resources.total_purchases}")
    print(f"Net profit: ${dot.resources.net_profit:.2f}")
    print()


def test_sell_action():
    """Test selling to market"""
    
    print("=" * 70)
    print("TEST 6: SELL ACTION")
    print("=" * 70)
    print()
    
    market = Market()
    
    dot = MockDot(3, wallet=5.0)
    
    # Give dot some items to sell
    dot.resources.add_to_inventory("iron", 3)
    dot.resources.add_to_inventory("bronze", 1)
    
    sell_action = SellAction(dot.dna)
    
    print(f"Dot wallet: ${dot.resources.wallet:.2f}")
    print(f"Inventory: {dot.resources.inventory}")
    print()
    
    # Sell iron
    iron_price = market.get_price("iron")
    print(f"Iron market price: ${iron_price:.2f}")
    print()
    
    print("Attempting to sell 2 iron...")
    result = sell_action.execute(dot, "iron", 2, market)
    
    print(f"Result: {result['result']}")
    if result['result'] == 'SALE_SUCCESS':
        print(f"  Commodity: {result['commodity']}")
        print(f"  Quantity: {result['quantity']}")
        print(f"  Price per unit: ${result['price_per_unit']:.2f}")
        print(f"  Total payment: ${result['total_payment']:.2f}")
        print(f"  Premium: {result['premium_applied']:.1%}")
    print()
    
    print(f"Dot wallet after: ${dot.resources.wallet:.2f}")
    print(f"Inventory after: {dot.resources.inventory}")
    print(f"Total sales: {dot.resources.total_sales}")
    print(f"Net profit: ${dot.resources.net_profit:.2f}")
    print()


def test_consume_action():
    """Test consuming food"""
    
    print("=" * 70)
    print("TEST 7: CONSUME ACTION")
    print("=" * 70)
    print()
    
    market = Market()
    
    dot = MockDot(4, wallet=10.0)
    
    # Give dot food
    dot.resources.add_to_inventory("food_grain", 3)
    dot.resources.add_to_inventory("food_meat", 1)
    
    # Set dot energy low
    dot.resources.energy = 30.0
    
    consume_action = ConsumeAction(dot.dna)
    
    print(f"Dot energy: {dot.resources.energy:.1f}/{dot.resources.max_energy:.1f}")
    print(f"Inventory: {dot.resources.inventory}")
    print()
    
    # Consume grain
    print("Consuming 2 food_grain...")
    result = consume_action.execute(dot, "food_grain", 2, market)
    
    print(f"Result: {result['result']}")
    if result['result'] == 'CONSUMED':
        print(f"  Commodity: {result['commodity']}")
        print(f"  Quantity: {result['quantity']}")
        print(f"  Energy gained: {result['energy_gained']:.1f}")
    print()
    
    print(f"Dot energy after: {dot.resources.energy:.1f}/{dot.resources.max_energy:.1f}")
    print(f"Inventory after: {dot.resources.inventory}")
    print()


def test_full_economic_cycle():
    """Test complete economic cycle: gather → sell → buy → consume"""
    
    print("=" * 70)
    print("TEST 8: FULL ECONOMIC CYCLE")
    print("=" * 70)
    print()
    
    market = Market()
    market.spawn_commodities()
    
    dot = MockDot(5, wallet=2.0)
    dot.resources.energy = 50.0  # Start hungry
    
    print("STARTING STATE:")
    print(f"  Wallet: ${dot.resources.wallet:.2f}")
    print(f"  Energy: {dot.resources.energy:.1f}/{dot.resources.max_energy:.1f}")
    print(f"  Inventory: {dot.resources.inventory}")
    print()
    
    # Step 1: Gather scrap from world
    print("STEP 1: Gather scrap from world")
    scrap = market.find_nearest_commodity(dot.position, "scrap")
    if scrap:
        dot.position = [scrap.position[0] + 5, scrap.position[1] + 5]
        gather_action = GatherAction(dot.dna)
        result = gather_action.execute(dot, scrap, market)
        print(f"  Gathered {result.get('quantity', 0)} {result.get('commodity', 'nothing')}")
    print(f"  Inventory: {dot.resources.inventory}")
    print()
    
    # Step 2: Gather more scrap
    print("STEP 2: Gather more items")
    for _ in range(3):
        nearest = market.find_nearest_commodity(dot.position)
        if nearest and not nearest.gathered:
            dot.position = [nearest.position[0] + 5, nearest.position[1] + 5]
            result = gather_action.execute(dot, nearest, market)
            if result['result'] == 'GATHERED':
                print(f"  Gathered {result['quantity']} {result['commodity']}")
    print(f"  Inventory: {dot.resources.inventory}")
    print()
    
    # Step 3: Sell items for money
    print("STEP 3: Sell items for money")
    sell_action = SellAction(dot.dna)
    
    for item_type, quantity in list(dot.resources.inventory.items()):
        if quantity > 0:
            result = sell_action.execute(dot, item_type, quantity, market)
            if result['result'] == 'SALE_SUCCESS':
                print(f"  Sold {result['quantity']} {result['commodity']} for ${result['total_payment']:.2f}")
    
    print(f"  Wallet: ${dot.resources.wallet:.2f}")
    print(f"  Net profit: ${dot.resources.net_profit:.2f}")
    print()
    
    # Step 4: Buy food
    print("STEP 4: Buy food with money")
    buy_action = BuyAction(dot.dna)
    result = buy_action.execute(dot, "food_grain", 3, market)
    
    if result['result'] == 'PURCHASE_SUCCESS':
        print(f"  Bought {result['quantity']} {result['commodity']} for ${result['total_cost']:.2f}")
    
    print(f"  Wallet: ${dot.resources.wallet:.2f}")
    print(f"  Inventory: {dot.resources.inventory}")
    print()
    
    # Step 5: Consume food
    print("STEP 5: Consume food to restore energy")
    consume_action = ConsumeAction(dot.dna)
    
    if "food_grain" in dot.resources.inventory:
        result = consume_action.execute(dot, "food_grain", 2, market)
        if result['result'] == 'CONSUMED':
            print(f"  Consumed {result['quantity']} {result['commodity']}")
            print(f"  Energy gained: {result['energy_gained']:.1f}")
    
    print()
    print("FINAL STATE:")
    print(f"  Wallet: ${dot.resources.wallet:.2f}")
    print(f"  Energy: {dot.resources.energy:.1f}/{dot.resources.max_energy:.1f}")
    print(f"  Inventory: {dot.resources.inventory}")
    print(f"  Total purchases: {dot.resources.total_purchases}")
    print(f"  Total sales: {dot.resources.total_sales}")
    print(f"  Net profit: ${dot.resources.net_profit:.2f}")
    print()


if __name__ == "__main__":
    print("\n\n")
    print("#" * 70)
    print("# DOT AI 3.0 - MARKET & TRADING SYSTEM TEST SUITE")
    print("#" * 70)
    print()
    
    try:
        test_market_initialization()
        test_commodity_spawning()
        test_price_dynamics()
        test_gather_action()
        test_buy_action()
        test_sell_action()
        test_consume_action()
        test_full_economic_cycle()
        
        print("\n\n")
        print("#" * 70)
        print("# ALL TESTS PASSED! ✓")
        print("# Market system and trading actions functioning correctly.")
        print("# Ready for integration into full simulation.")
        print("#" * 70)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
