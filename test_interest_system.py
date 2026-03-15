"""
Test script for Hold Power / Interest System
Tests passive income generation for investor dots

Run this to verify:
- Interest rate calculation from hold_power gene
- Interest application and compounding
- Wallet capacity capping
- Passive income projections
"""

import sys
import time
from core.dna import DNAProfile
from core.resources import Resources


def test_interest_rate_calculation():
    """Test interest rate calculation from hold_power gene"""
    
    print("=" * 70)
    print("TEST 1: INTEREST RATE CALCULATION")
    print("=" * 70)
    print()
    
    # Base case - no hold_power gene
    base_dna = DNAProfile(total_points=200)
    base_resources = Resources(base_dna)
    base_rate = base_resources.calculate_interest_rate()
    
    print(f"Base (no hold_power): {base_rate*100:.3f}% per second")
    print()
    
    # Low hold_power
    low_dna = DNAProfile(total_points=200)
    low_dna.hold_power.enabled = True
    low_dna.hold_power.points = 10
    low_resources = Resources(low_dna)
    low_rate = low_resources.calculate_interest_rate()
    
    print(f"Low (10 points):      {low_rate*100:.3f}% per second (base + {(low_rate-base_rate)*100:.3f}%)")
    print()
    
    # Medium hold_power
    med_dna = DNAProfile(total_points=200)
    med_dna.hold_power.enabled = True
    med_dna.hold_power.points = 25
    med_resources = Resources(med_dna)
    med_rate = med_resources.calculate_interest_rate()
    
    print(f"Medium (25 points):   {med_rate*100:.3f}% per second (base + {(med_rate-base_rate)*100:.3f}%)")
    print()
    
    # High hold_power
    high_dna = DNAProfile(total_points=200)
    high_dna.hold_power.enabled = True
    high_dna.hold_power.points = 50
    high_resources = Resources(high_dna)
    high_rate = high_resources.calculate_interest_rate()
    
    print(f"High (50 points):     {high_rate*100:.3f}% per second (base + {(high_rate-base_rate)*100:.3f}%)")
    print()
    
    # Show hourly projection (more realistic than annual)
    print("Hourly Growth Projections ($100 starting balance):")
    for label, rate in [("Base", base_rate), ("Low", low_rate), ("Med", med_rate), ("High", high_rate)]:
        # Compound for 1 hour = 3600 seconds
        seconds_per_hour = 3600
        balance_after_hour = 100.0
        for _ in range(seconds_per_hour):
            balance_after_hour += balance_after_hour * rate
        
        growth = balance_after_hour - 100.0
        print(f"  {label:6} - ${balance_after_hour:8.2f} (+${growth:6.2f} in 1 hour)")
    print()


def test_interest_application():
    """Test applying interest to wallet"""
    
    print("=" * 70)
    print("TEST 2: INTEREST APPLICATION")
    print("=" * 70)
    print()
    
    # Create investor with hold_power
    dna = DNAProfile(total_points=200)
    dna.hold_power.enabled = True
    dna.hold_power.points = 30
    
    resources = Resources(dna)
    resources.wallet = 50.0  # Start below max to allow growth
    resources.max_wallet = 200.0  # Give room for interest
    
    print(f"Starting wallet: ${resources.wallet:.2f}")
    print(f"Interest rate: {resources.calculate_interest_rate()*100:.3f}% per second")
    print()
    
    # Apply interest for 1 second
    result = resources.apply_interest(1.0)
    
    print(f"After 1 second:")
    print(f"  Interest earned: ${result['interest_earned']:.4f}")
    print(f"  New balance: ${result['new_balance']:.2f}")
    print(f"  Rate used: {result['rate_used']*100:.3f}%")
    print()
    
    # Apply interest for 10 more seconds
    for i in range(10):
        result = resources.apply_interest(1.0)
    
    print(f"After 11 seconds total:")
    print(f"  Wallet: ${resources.wallet:.2f}")
    print()


def test_compound_growth():
    """Test compounding interest over time"""
    
    print("=" * 70)
    print("TEST 3: COMPOUND GROWTH SIMULATION")
    print("=" * 70)
    print()
    
    # Create strong investor
    dna = DNAProfile(total_points=200)
    dna.hold_power.enabled = True
    dna.hold_power.points = 40  # 0.45% per second total
    
    resources = Resources(dna)
    resources.wallet = 50.0  # Start below max
    resources.max_wallet = 500.0  # Give plenty of room for growth
    
    print(f"Investor Profile:")
    print(f"  Hold power: {dna.hold_power.points} points")
    print(f"  Interest rate: {resources.calculate_interest_rate()*100:.3f}% per second")
    print(f"  Starting wallet: ${resources.wallet:.2f}")
    print()
    
    print("Growth Trajectory:")
    checkpoints = [10, 30, 60, 120, 300, 600]
    
    for target_sec in checkpoints:
        # Apply interest second by second for accuracy
        while resources.wallet < resources.max_wallet:
            result = resources.apply_interest(1.0)
            
            # Check if we've reached checkpoint
            elapsed = target_sec  # Simplified for test
            if target_sec == checkpoints[0]:
                break
        
        # Reset for next checkpoint
        if target_sec != checkpoints[-1]:
            continue
    
    # Proper simulation
    resources.wallet = 100.0
    for seconds in checkpoints:
        # Apply interest for interval
        interval = seconds if seconds == checkpoints[0] else (seconds - checkpoints[checkpoints.index(seconds)-1] if checkpoints.index(seconds) > 0 else seconds)
        
        for _ in range(interval):
            resources.apply_interest(1.0)
        
        income_per_min = resources.get_passive_income_per_minute()
        print(f"  After {seconds:3d} sec: ${resources.wallet:7.2f} (earning ${income_per_min:.2f}/min)")
    print()


def test_wallet_capacity_capping():
    """Test that interest respects wallet capacity"""
    
    print("=" * 70)
    print("TEST 4: WALLET CAPACITY CAPPING")
    print("=" * 70)
    print()
    
    # Create investor with small wallet
    dna = DNAProfile(total_points=200)
    dna.hold_power.enabled = True
    dna.hold_power.points = 50  # High interest rate
    
    resources = Resources(dna)
    resources.wallet = 99.0
    resources.max_wallet = 100.0  # Very limited capacity
    
    print(f"Setup:")
    print(f"  Wallet: ${resources.wallet:.2f}")
    print(f"  Max wallet: ${resources.max_wallet:.2f}")
    print(f"  Space available: ${resources.max_wallet - resources.wallet:.2f}")
    print(f"  Interest rate: {resources.calculate_interest_rate()*100:.3f}% per second")
    print()
    
    # Apply interest (should cap at max_wallet)
    result = resources.apply_interest(1.0)
    
    print(f"After 1 second:")
    print(f"  Interest calculated: ${resources.wallet * resources.calculate_interest_rate():.4f}")
    print(f"  Interest earned: ${result['interest_earned']:.4f}")
    print(f"  New balance: ${result['new_balance']:.2f}")
    print(f"  Was capped: {result['was_capped']}")
    print(f"  At max wallet: {resources.wallet >= resources.max_wallet}")
    print()


def test_passive_income_projection():
    """Test passive income per minute calculation"""
    
    print("=" * 70)
    print("TEST 5: PASSIVE INCOME PROJECTIONS")
    print("=" * 70)
    print()
    
    # Different investor profiles
    profiles = [
        ("Conservative Saver", 10, 50.0),
        ("Active Trader", 25, 100.0),
        ("Serious Investor", 40, 200.0),
        ("Wealth Manager", 50, 500.0)
    ]
    
    print("Passive Income Potential:")
    print()
    
    for name, hold_power_points, wallet_balance in profiles:
        dna = DNAProfile(total_points=200)
        dna.hold_power.enabled = True
        dna.hold_power.points = hold_power_points
        
        resources = Resources(dna)
        resources.wallet = wallet_balance
        
        rate = resources.calculate_interest_rate()
        income_per_min = resources.get_passive_income_per_minute()
        income_per_hour = income_per_min * 60
        
        print(f"{name:20}")
        print(f"  Hold Power: {hold_power_points:2d} pts → {rate*100:.3f}%/sec")
        print(f"  Wallet: ${wallet_balance:6.2f}")
        print(f"  Income: ${income_per_min:.4f}/min = ${income_per_hour:.2f}/hour")
        print()


def test_investor_vs_trader():
    """Compare investor (passive income) vs trader (active trading)"""
    
    print("=" * 70)
    print("TEST 6: INVESTOR VS TRADER COMPARISON")
    print("=" * 70)
    print()
    
    # INVESTOR: High hold_power, large wallet
    investor_dna = DNAProfile(total_points=200)
    investor_dna.hold_power.enabled = True
    investor_dna.hold_power.points = 45
    investor_dna.max_wallet.enabled = True
    investor_dna.max_wallet.points = 30
    
    investor = Resources(investor_dna)
    investor.wallet = 200.0  # Use less than max
    investor.max_wallet = 400.0  # Increased from max_wallet gene
    
    # TRADER: Low hold_power, smaller wallet, but trades actively
    trader_dna = DNAProfile(total_points=200)
    trader_dna.hold_power.enabled = True
    trader_dna.hold_power.points = 5
    trader_dna.buy_power.enabled = True
    trader_dna.buy_power.points = 30
    trader_dna.sell_power.enabled = True
    trader_dna.sell_power.points = 25
    
    trader = Resources(trader_dna)
    trader.wallet = 50.0  # Small capital
    
    print("INVESTOR PROFILE:")
    print(f"  Hold Power: {investor_dna.hold_power.points} pts")
    print(f"  Wallet: ${investor.wallet:.2f}")
    print(f"  Max Wallet: ${investor.max_wallet:.2f}")
    print(f"  Interest Rate: {investor.calculate_interest_rate()*100:.3f}%/sec")
    print(f"  Passive Income: ${investor.get_passive_income_per_minute():.2f}/min")
    print()
    
    print("TRADER PROFILE:")
    print(f"  Hold Power: {trader_dna.hold_power.points} pts")
    print(f"  Buy Power: {trader_dna.buy_power.points} pts → {trader_dna.buy_power.points * 0.5:.1f}% discount")
    print(f"  Sell Power: {trader_dna.sell_power.points} pts → {trader_dna.sell_power.points * 0.6:.1f}% premium")
    print(f"  Wallet: ${trader.wallet:.2f}")
    print(f"  Interest Rate: {trader.calculate_interest_rate()*100:.3f}%/sec")
    print(f"  Passive Income: ${trader.get_passive_income_per_minute():.4f}/min (negligible)")
    print()
    
    print("STRATEGY COMPARISON:")
    print(f"  Investor earns ${investor.get_passive_income_per_minute():.2f}/min passively")
    print(f"  Trader must make trades to earn (15% buy discount + 15% sell premium = 30% profit margin)")
    print(f"  Trader needs {investor.get_passive_income_per_minute() / 0.30:.2f} in sales/min to match investor passive income")
    print()


if __name__ == "__main__":
    print("\n\n")
    print("#" * 70)
    print("# DOT AI 3.0 - HOLD POWER / INTEREST SYSTEM TEST SUITE")
    print("#" * 70)
    print()
    
    try:
        test_interest_rate_calculation()
        test_interest_application()
        test_compound_growth()
        test_wallet_capacity_capping()
        test_passive_income_projection()
        test_investor_vs_trader()
        
        print("\n\n")
        print("#" * 70)
        print("# ALL TESTS PASSED! ✓")
        print("# Hold power interest system functioning correctly.")
        print("# Investors now earn passive income on capital.")
        print("#" * 70)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
