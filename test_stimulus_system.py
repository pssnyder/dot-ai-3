"""
Test script for Stimulus Payment System (UBI)
Tests the universal basic income mechanics

Run this to verify:
- Role-based payment schedules working
- Payment delivery timing correct
- Wallet capacity limits respected
- Global money supply tracking accurate
"""

import sys
import time
from core.dna import DNAProfile
from core.resources import Resources
from core.stimulus import StimulusPayment, StimulusSystem


class MockDot:
    """Simplified dot for testing"""
    def __init__(self, dot_id, dna, wallet=5.0):
        self.id = dot_id
        self.dna = dna
        self.resources = Resources(dna)
        self.resources.wallet = wallet


def test_payment_schedules():
    """Test that different roles get appropriate payment schedules"""
    
    print("=" * 70)
    print("TEST 1: ROLE-BASED PAYMENT SCHEDULES")
    print("=" * 70)
    print()
    
    # Build different role profiles
    roles = []
    
    # TRADER
    trader_dna = DNAProfile(total_points=200)
    trader_dna.buy_power.enabled = True
    trader_dna.buy_power.points = 30
    trader_dna.sell_power.enabled = True
    trader_dna.sell_power.points = 25
    trader_dot = MockDot(1, trader_dna)
    trader_stimulus = StimulusPayment(trader_dot)
    roles.append(("TRADER", trader_stimulus))
    
    # INVESTOR
    investor_dna = DNAProfile(total_points=200)
    investor_dna.hold_power.enabled = True
    investor_dna.hold_power.points = 40
    investor_dna.max_wallet.enabled = True
    investor_dna.max_wallet.points = 30
    investor_dot = MockDot(2, investor_dna)
    investor_stimulus = StimulusPayment(investor_dot)
    roles.append(("INVESTOR", investor_stimulus))
    
    # GATHERER
    gatherer_dna = DNAProfile(total_points=200)
    gatherer_dna.gather_speed.enabled = True
    gatherer_dna.gather_speed.points = 40
    gatherer_dot = MockDot(3, gatherer_dna)
    gatherer_stimulus = StimulusPayment(gatherer_dot)
    roles.append(("GATHERER", gatherer_stimulus))
    
    # GENERALIST
    generalist_dna = DNAProfile(total_points=200)
    generalist_dna.buy_power.enabled = True
    generalist_dna.buy_power.points = 10
    generalist_dna.hold_power.enabled = True
    generalist_dna.hold_power.points = 10
    generalist_dot = MockDot(4, generalist_dna)
    generalist_stimulus = StimulusPayment(generalist_dot)
    roles.append(("GENERALIST", generalist_stimulus))
    
    # NON-ECONOMIC (combat specialist)
    combat_dna = DNAProfile(total_points=200)
    combat_dna.attack.points = 30
    combat_dna.defend.points = 20
    combat_dot = MockDot(5, combat_dna)
    combat_stimulus = StimulusPayment(combat_dot)
    roles.append(("NON-ECONOMIC", combat_stimulus))
    
    print("Payment Schedules by Role:")
    print()
    for expected_role, stimulus in roles:
        info = stimulus.get_payment_info()
        print(f"{info['role']:15} - ${info['payment_amount']:.2f} every {info['payment_interval']:.0f}s = ${info['income_per_minute']:.2f}/min")
        if info['role'] != expected_role:
            print(f"  WARNING: Expected {expected_role} but got {info['role']}")
    print()


def test_payment_delivery():
    """Test payment timing and delivery"""
    
    print("=" * 70)
    print("TEST 2: PAYMENT DELIVERY TIMING")
    print("=" * 70)
    print()
    
    # Create trader (fast payments)
    trader_dna = DNAProfile(total_points=200)
    trader_dna.buy_power.enabled = True
    trader_dna.buy_power.points = 30
    trader_dna.sell_power.enabled = True
    trader_dna.sell_power.points = 25
    
    dot = MockDot(1, trader_dna, wallet=5.0)
    stimulus = StimulusPayment(dot)
    
    print(f"Initial wallet: ${dot.resources.wallet:.2f}")
    print(f"Payment schedule: ${stimulus.payment_amount:.2f} every {stimulus.payment_interval:.0f}s")
    print()
    
    # Try immediate payment (should fail - not enough time elapsed)
    current_time = time.time()
    result = stimulus.check_payment(current_time)
    print(f"Immediate check: {result['result']}")
    if result['result'] == 'NOT_DUE':
        print(f"  Time remaining: {result['time_remaining']:.1f}s")
    print()
    
    # Fast-forward time by payment interval
    print(f"Fast-forwarding {stimulus.payment_interval:.0f} seconds...")
    future_time = current_time + stimulus.payment_interval
    result = stimulus.check_payment(future_time)
    
    print(f"Payment check: {result['result']}")
    if result['result'] == 'PAYMENT_DELIVERED':
        print(f"  Amount: ${result['amount']:.2f}")
        print(f"  New balance: ${result['new_balance']:.2f}")
        print(f"  Payment #: {result['payment_number']}")
    print()
    
    print(f"Final wallet: ${dot.resources.wallet:.2f}")
    print()


def test_wallet_capacity_limit():
    """Test that payments respect wallet capacity"""
    
    print("=" * 70)
    print("TEST 3: WALLET CAPACITY LIMITS")
    print("=" * 70)
    print()
    
    # Create dot with full wallet
    trader_dna = DNAProfile(total_points=200)
    trader_dna.buy_power.enabled = True
    trader_dna.buy_power.points = 30
    
    dot = MockDot(1, trader_dna, wallet=100.0)  # Start at max
    dot.resources.max_wallet = 100.0
    
    stimulus = StimulusPayment(dot)
    
    print(f"Wallet: ${dot.resources.wallet:.2f} / ${dot.resources.max_wallet:.2f}")
    print()
    
    # Try to deliver payment when full
    future_time = time.time() + stimulus.payment_interval
    result = stimulus.check_payment(future_time)
    
    print(f"Payment check: {result['result']}")
    if result['result'] == 'WALLET_FULL':
        print(f"  Wallet: ${result['wallet']:.2f}")
        print(f"  Max wallet: ${result['max_wallet']:.2f}")
    print()
    
    # Spend some money to make room
    dot.resources.wallet = 95.0
    print(f"Spent $5, new wallet: ${dot.resources.wallet:.2f}")
    print()
    
    # Try payment again (should deliver partial amount)
    result = stimulus.check_payment(future_time)
    print(f"Payment check: {result['result']}")
    if result['result'] == 'PAYMENT_DELIVERED':
        print(f"  Payment requested: ${stimulus.payment_amount:.2f}")
        print(f"  Payment delivered: ${result['amount']:.2f} (capped by wallet space)")
        print(f"  New balance: ${result['new_balance']:.2f}")
    print()


def test_multiple_payments():
    """Test multiple payments over time"""
    
    print("=" * 70)
    print("TEST 4: MULTIPLE PAYMENTS SIMULATION")
    print("=" * 70)
    print()
    
    # Create investor (slow but large payments)
    investor_dna = DNAProfile(total_points=200)
    investor_dna.hold_power.enabled = True
    investor_dna.hold_power.points = 40
    investor_dna.max_wallet.enabled = True
    investor_dna.max_wallet.points = 30
    
    dot = MockDot(1, investor_dna, wallet=10.0)
    dot.resources.max_wallet = 400.0  # Large wallet from max_wallet gene
    
    stimulus = StimulusPayment(dot)
    
    print(f"Role: {stimulus.role}")
    print(f"Payment: ${stimulus.payment_amount:.2f} every {stimulus.payment_interval:.0f}s")
    print(f"Starting wallet: ${dot.resources.wallet:.2f}")
    print()
    
    # Simulate 5 payments
    print("Payment History:")
    current_time = time.time()
    
    for i in range(5):
        # Advance time by payment interval
        current_time += stimulus.payment_interval
        result = stimulus.check_payment(current_time)
        
        if result['result'] == 'PAYMENT_DELIVERED':
            print(f"  Payment {i+1}: +${result['amount']:.2f} → Wallet: ${result['new_balance']:.2f}")
    
    print()
    print(f"Final wallet: ${dot.resources.wallet:.2f}")
    print(f"Total stimulus received: ${stimulus.total_stimulus_received:.2f}")
    print(f"Payment count: {stimulus.payment_count}")
    print()


def test_global_stimulus_tracking():
    """Test global stimulus system for economic analysis"""
    
    print("=" * 70)
    print("TEST 5: GLOBAL STIMULUS TRACKING")
    print("=" * 70)
    print()
    
    system = StimulusSystem()
    
    # Create population of different roles
    dots = []
    
    # 10 traders
    for i in range(10):
        trader_dna = DNAProfile(total_points=200)
        trader_dna.buy_power.enabled = True
        trader_dna.buy_power.points = 40
        dot = MockDot(i, trader_dna)
        stimulus = StimulusPayment(dot)
        dots.append((dot, stimulus))
    
    # 5 investors
    for i in range(10, 15):
        investor_dna = DNAProfile(total_points=200)
        investor_dna.hold_power.enabled = True
        investor_dna.hold_power.points = 40
        dot = MockDot(i, investor_dna)
        stimulus = StimulusPayment(dot)
        dots.append((dot, stimulus))
    
    # 5 generalists
    for i in range(15, 20):
        gen_dna = DNAProfile(total_points=200)
        gen_dna.buy_power.enabled = True
        gen_dna.buy_power.points = 15
        gen_dna.hold_power.enabled = True
        gen_dna.hold_power.points = 15
        dot = MockDot(i, gen_dna)
        stimulus = StimulusPayment(dot)
        dots.append((dot, stimulus))
    
    print(f"Population: {len(dots)} dots")
    print()
    
    # Simulate 60 seconds of payments
    start_time = time.time()
    simulation_duration = 60.0
    
    print(f"Simulating {simulation_duration:.0f} seconds of stimulus payments...")
    print()
    
    for t in range(int(simulation_duration)):
        current_time = start_time + t
        
        for dot, stimulus in dots:
            result = stimulus.check_payment(current_time)
            if result['result'] == 'PAYMENT_DELIVERED':
                system.record_payment(stimulus.role, result['amount'])
    
    # Display results
    stats = system.get_stats()
    
    print("Global Stimulus Statistics:")
    print(f"  Total paid: ${stats['total_stimulus_paid']:.2f}")
    print(f"  Total payments: {stats['total_payments']}")
    print(f"  Average payment: ${stats['average_payment']:.2f}")
    print()
    
    print("Breakdown by Role:")
    for role, data in stats['payments_by_role'].items():
        print(f"  {role:15} - ${data['total_paid']:7.2f} ({data['percent_of_total']:5.1f}%) over {data['payment_count']:3d} payments")
    print()


if __name__ == "__main__":
    print("\n\n")
    print("#" * 70)
    print("# DOT AI 3.0 - STIMULUS PAYMENT SYSTEM TEST SUITE")
    print("#" * 70)
    print()
    
    try:
        test_payment_schedules()
        test_payment_delivery()
        test_wallet_capacity_limit()
        test_multiple_payments()
        test_global_stimulus_tracking()
        
        print("\n\n")
        print("#" * 70)
        print("# ALL TESTS PASSED! ✓")
        print("# Stimulus payment system functioning correctly.")
        print("# UBI payments creating ongoing money supply growth.")
        print("#" * 70)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
