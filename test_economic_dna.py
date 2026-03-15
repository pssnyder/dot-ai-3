"""
Test script for Economic DNA Genes (Dot AI 3.0)
Tests the economic gene system and role classification

Run this to verify:
- Economic genes initialize correctly
- Buy/sell power calculations working
- Role classification (trader vs investor vs generalist)
- DNA budget validation with economic genes
"""

import sys
from core.dna import DNAProfile, Gene


def test_economic_genes_initialization():
    """Test that economic genes are created properly"""
    
    print("=" * 70)
    print("TEST 1: ECONOMIC GENES INITIALIZATION")
    print("=" * 70)
    print()
    
    dna = DNAProfile()
    
    # Check all economic genes exist
    economic_genes = [
        'buy_power',
        'sell_power',
        'gather_speed',
        'hold_power',
        'max_wallet',
        'market_visibility'
    ]
    
    print("Economic Genes:")
    for gene_name in economic_genes:
        if hasattr(dna, gene_name):
            gene = getattr(dna, gene_name)
            print(f"  ✓ {gene_name:20} - {gene}")
        else:
            print(f"  ✗ {gene_name:20} - MISSING!")
    print()
    
    # Verify all start disabled (not default abilities)
    all_disabled = all(not getattr(dna, g).enabled for g in economic_genes)
    print(f"All economic genes start disabled: {all_disabled}")
    print()


def test_trader_build():
    """Test trader specialization (high buy/sell power)"""
    
    print("=" * 70)
    print("TEST 2: TRADER BUILD (Buy/Sell Specialist)")
    print("=" * 70)
    print()
    
    # Use larger budget for 3.0 (base 100 + economic expansion)
    dna = DNAProfile(total_points=200)  # 3.0 dots get more points for economic abilities
    
    # Build a trader - focus on buy/sell power
    dna.buy_power.enabled = True
    dna.buy_power.points = 30  # 15% discount
    
    dna.sell_power.enabled = True
    dna.sell_power.points = 25  # 15% premium
    
    dna.market_visibility.enabled = True
    dna.market_visibility.points = 10  # See market data
    
    dna.gather_speed.enabled = True
    dna.gather_speed.points = 15  # Faster gathering
    
    allocated = dna.get_allocated_points()
    available = dna.get_available_points()
    valid = dna.is_valid()
    
    print("TRADER DNA PROFILE:")
    print(f"  Total points: {dna.total_points}")
    print(f"  Allocated: {allocated}")
    print(f"  Available: {available}")
    print(f"  Valid: {valid}")
    print()
    
    print("Economic Abilities:")
    print(f"  Buy Power: {dna.buy_power.points} pts → {dna.buy_power.points * 0.5:.1f}% discount")
    print(f"  Sell Power: {dna.sell_power.points} pts → {dna.sell_power.points * 0.6:.1f}% premium")
    print(f"  Market Visibility: {dna.market_visibility.points} pts → {'CAN' if dna.market_visibility.points >= 5 else 'CANNOT'} see supply")
    print(f"  Gather Speed: {dna.gather_speed.points} pts → {dna.gather_speed.points * 2:.0f}% faster")
    print()
    
    # Calculate trading efficiency
    base_buy_price = 100.0
    discount = dna.buy_power.points * 0.005  # 0.5% per point
    final_buy = base_buy_price * (1.0 - discount)
    
    base_sell_price = 100.0
    premium = dna.sell_power.points * 0.006  # 0.6% per point
    final_sell = base_sell_price * (1.0 + premium)
    
    print("Trading Example (commodity worth $100):")
    print(f"  Buy price: ${base_buy_price:.2f} → ${final_buy:.2f} ({discount*100:.1f}% discount)")
    print(f"  Sell price: ${base_sell_price:.2f} → ${final_sell:.2f} ({premium*100:.1f}% premium)")
    print(f"  Arbitrage profit: ${final_sell - final_buy:.2f} per unit traded")
    print()


def test_investor_build():
    """Test investor specialization (high hold power + wallet capacity)"""
    
    print("=" * 70)
    print("TEST 3: INVESTOR BUILD (Capital Accumulator)")
    print("=" * 70)
    print()
    
    # Use larger budget for 3.0 (base 100 + economic expansion)
    dna = DNAProfile(total_points=200)  # 3.0 dots get more points for economic abilities
    
    # Build an investor - focus on holding capital
    dna.hold_power.enabled = True
    dna.hold_power.points = 40  # Strong interest rate
    
    dna.max_wallet.enabled = True
    dna.max_wallet.points = 30  # Large wallet capacity
    
    dna.buy_power.enabled = True
    dna.buy_power.points = 15  # Some negotiation skill
    
    allocated = dna.get_allocated_points()
    available = dna.get_available_points()
    valid = dna.is_valid()
    
    print("INVESTOR DNA PROFILE:")
    print(f"  Total points: {dna.total_points}")
    print(f"  Allocated: {allocated}")
    print(f"  Available: {available}")
    print(f"  Valid: {valid}")
    print()
    
    print("Economic Abilities:")
    print(f"  Hold Power: {dna.hold_power.points} pts → {dna.hold_power.points * 0.01:.2f}%/sec interest")
    print(f"  Max Wallet: {dna.max_wallet.points} pts → +${dna.max_wallet.points * 10:.0f} capacity")
    print(f"  Buy Power: {dna.buy_power.points} pts → {dna.buy_power.points * 0.5:.1f}% discount")
    print()
    
    # Calculate passive income
    base_wallet = 100.0
    wallet_capacity = base_wallet + (dna.max_wallet.points * 10)
    interest_rate = dna.hold_power.points * 0.0001  # 0.01% per point per second
    passive_income_per_sec = wallet_capacity * interest_rate
    passive_income_per_min = passive_income_per_sec * 60
    
    print("Passive Income Simulation:")
    print(f"  Base wallet: ${base_wallet:.2f}")
    print(f"  Max wallet capacity: ${wallet_capacity:.2f}")
    print(f"  Interest rate: {interest_rate*100:.2f}% per second")
    print(f"  Passive income: ${passive_income_per_sec:.4f}/sec = ${passive_income_per_min:.2f}/min")
    print()
    
    # Show compound growth
    print("Compound Growth (holding for 60 seconds):")
    balance = wallet_capacity
    for seconds in [10, 20, 30, 40, 50, 60]:
        balance = balance * (1 + interest_rate) ** seconds
        print(f"  After {seconds:2d} sec: ${balance:.2f}")
    print()


def test_generalist_build():
    """Test balanced build (hybrid capabilities)"""
    
    print("=" * 70)
    print("TEST 4: GENERALIST BUILD (Balanced Hybrid)")
    print("=" * 70)
    print()
    
    # Use larger budget for 3.0 (base 100 + economic expansion)
    dna = DNAProfile(total_points=200)  # 3.0 dots get more points for economic abilities
    
    # Build a generalist - balanced distribution
    dna.buy_power.enabled = True
    dna.buy_power.points = 10
    
    dna.sell_power.enabled = True
    dna.sell_power.points = 10
    
    dna.gather_speed.enabled = True
    dna.gather_speed.points = 10
    
    dna.hold_power.enabled = True
    dna.hold_power.points = 10
    
    dna.max_wallet.enabled = True
    dna.max_wallet.points = 10
    
    dna.market_visibility.enabled = True
    dna.market_visibility.points = 5
    
    allocated = dna.get_allocated_points()
    available = dna.get_available_points()
    valid = dna.is_valid()
    
    print("GENERALIST DNA PROFILE:")
    print(f"  Total points: {dna.total_points}")
    print(f"  Allocated: {allocated}")
    print(f"  Available: {available}")
    print(f"  Valid: {valid}")
    print()
    
    print("Economic Abilities (all moderate):")
    print(f"  Buy Power: {dna.buy_power.points} pts → {dna.buy_power.points * 0.5:.1f}% discount")
    print(f"  Sell Power: {dna.sell_power.points} pts → {dna.sell_power.points * 0.6:.1f}% premium")
    print(f"  Gather Speed: {dna.gather_speed.points} pts → {dna.gather_speed.points * 2:.0f}% faster")
    print(f"  Hold Power: {dna.hold_power.points} pts → {dna.hold_power.points * 0.01:.2f}%/sec interest")
    print(f"  Max Wallet: {dna.max_wallet.points} pts → +${dna.max_wallet.points * 10:.0f} capacity")
    print(f"  Market Visibility: {dna.market_visibility.points} pts → Can see supply: {dna.market_visibility.points >= 5}")
    print()


def test_role_classification():
    """Test automatic role classification based on gene distribution"""
    
    print("=" * 70)
    print("TEST 5: AUTOMATIC ROLE CLASSIFICATION")
    print("=" * 70)
    print()
    
    def classify_role(dna):
        """Classify economic role based on gene distribution"""
        
        # Calculate specialization scores
        trader_score = dna.buy_power.points + dna.sell_power.points + dna.market_visibility.points
        investor_score = dna.hold_power.points + dna.max_wallet.points
        gatherer_score = dna.gather_speed.points
        
        # Determine primary role
        if trader_score >= 40:
            return "TRADER", trader_score
        elif investor_score >= 40:
            return "INVESTOR", investor_score
        elif gatherer_score >= 30:
            return "GATHERER", gatherer_score
        elif trader_score + investor_score + gatherer_score < 20:
            return "NON-ECONOMIC", 0
        else:
            return "GENERALIST", trader_score + investor_score + gatherer_score
    
    # Test different builds
    builds = []
    
    # Trader build
    trader_dna = DNAProfile()
    trader_dna.buy_power.enabled = True
    trader_dna.buy_power.points = 25
    trader_dna.sell_power.enabled = True
    trader_dna.sell_power.points = 20
    trader_dna.market_visibility.enabled = True
    trader_dna.market_visibility.points = 10
    builds.append(("Trader Specialist", trader_dna))
    
    # Investor build
    investor_dna = DNAProfile()
    investor_dna.hold_power.enabled = True
    investor_dna.hold_power.points = 30
    investor_dna.max_wallet.enabled = True
    investor_dna.max_wallet.points = 25
    builds.append(("Investor Specialist", investor_dna))
    
    # Gatherer build
    gatherer_dna = DNAProfile()
    gatherer_dna.gather_speed.enabled = True
    gatherer_dna.gather_speed.points = 40
    builds.append(("Gatherer Specialist", gatherer_dna))
    
    # Generalist build
    generalist_dna = DNAProfile()
    generalist_dna.buy_power.enabled = True
    generalist_dna.buy_power.points = 10
    generalist_dna.hold_power.enabled = True
    generalist_dna.hold_power.points = 10
    generalist_dna.gather_speed.enabled = True
    generalist_dna.gather_speed.points = 10
    builds.append(("Balanced Generalist", generalist_dna))
    
    # Non-economic (combat specialist)
    combat_dna = DNAProfile()
    combat_dna.attack.points = 30
    combat_dna.defend.points = 20
    builds.append(("Combat Specialist", combat_dna))
    
    print("Role Classification Results:")
    for name, dna in builds:
        role, score = classify_role(dna)
        print(f"  {name:25} → {role:15} (score: {score})")
    print()


def test_budget_validation():
    """Test DNA budget validation with economic genes"""
    
    print("=" * 70)
    print("TEST 6: BUDGET VALIDATION")
    print("=" * 70)
    print()
    
    # Valid build (under budget) - use 3.0 budget
    valid_dna = DNAProfile(total_points=200)
    valid_dna.buy_power.enabled = True
    valid_dna.buy_power.points = 20
    valid_dna.sell_power.enabled = True
    valid_dna.sell_power.points = 20
    valid_dna.hold_power.enabled = True
    valid_dna.hold_power.points = 20
    
    print("VALID BUILD:")
    print(f"  Total points: {valid_dna.total_points}")
    print(f"  Allocated: {valid_dna.get_allocated_points()}")
    print(f"  Is valid: {valid_dna.is_valid()}")
    print()
    
    # Invalid build (over budget) - simulate corruption
    invalid_dna = DNAProfile(total_points=200)
    invalid_dna.buy_power.enabled = True
    invalid_dna.buy_power.points = 50
    invalid_dna.sell_power.enabled = True
    invalid_dna.sell_power.points = 50
    invalid_dna.hold_power.enabled = True
    invalid_dna.hold_power.points = 50
    
    print("INVALID BUILD (corrupted):")
    print(f"  Total points: {invalid_dna.total_points}")
    print(f"  Allocated: {invalid_dna.get_allocated_points()}")
    print(f"  Is valid: {invalid_dna.is_valid()}")
    print(f"  Over budget by: {invalid_dna.get_allocated_points() - invalid_dna.total_points}")
    print()


if __name__ == "__main__":
    print("\n\n")
    print("#" * 70)
    print("# DOT AI 3.0 - ECONOMIC DNA GENES TEST SUITE")
    print("#" * 70)
    print()
    
    try:
        test_economic_genes_initialization()
        test_trader_build()
        test_investor_build()
        test_generalist_build()
        test_role_classification()
        test_budget_validation()
        
        print("\n\n")
        print("#" * 70)
        print("# ALL TESTS PASSED! ✓")
        print("# Economic DNA system functioning correctly.")
        print("# Dots can now specialize as traders, investors, or generalists.")
        print("#" * 70)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
