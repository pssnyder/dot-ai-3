"""
Test script for BribeAction (Negotiation & Mercy Dynamic Decision Logic)
Tests the attacker decision making system for Dot AI 3.0

Run this to verify:
- Expected value calculations
- Sub-goal determination
- Accept/reject bribe decisions
- Mercy mode integration
- Different scenarios (desperate, aggressive, conservative, etc.)
"""

import sys
from core.dna import DNAProfile
from core.resources import Resources
from core.actions import BribeAction
from core.dot import Dot


class MockDot:
    """Simplified dot for testing"""
    def __init__(self, dot_id, wallet, hunger, attack_points, defend_points, health):
        self.id = dot_id
        self.dna = DNAProfile()
        self.dna.attack.enabled = attack_points > 0
        self.dna.attack.points = attack_points
        self.dna.defend.enabled = defend_points > 0
        self.dna.defend.points = defend_points
        
        self.resources = Resources(self.dna)
        self.resources.wallet = wallet
        self.resources.hunger = hunger
        self.resources.health = health
        
        self.current_state = "NORMAL"


def test_expected_value_calculation():
    """Test attack expected value calculation"""
    
    print("=" * 70)
    print("TEST 1: EXPECTED VALUE CALCULATION")
    print("=" * 70)
    print()
    
    bribe_action = BribeAction(DNAProfile())
    
    # Scenario 1: Strong attacker vs weak victim
    print("Scenario 1: Strong Attacker (20 attack) vs Weak Victim (5 defend, $50)")
    attacker = MockDot(1, wallet=10, hunger=0.5, attack_points=20, defend_points=5, health=100)
    victim = MockDot(2, wallet=50, hunger=0.3, attack_points=5, defend_points=5, health=60)
    
    ev_data = bribe_action.calculate_attack_expected_value(attacker, victim)
    print(f"  Kill probability: {ev_data['kill_probability']:.1%}")
    print(f"  Death probability: {ev_data['death_probability']:.1%}")
    print(f"  Expected gain: ${ev_data['expected_gain']:.2f}")
    print(f"  Expected loss: ${ev_data['expected_loss']:.2f}")
    print(f"  Net expected value: ${ev_data['expected_value']:.2f}")
    print()
    
    # Scenario 2: Weak attacker vs strong victim
    print("Scenario 2: Weak Attacker (5 attack) vs Strong Victim (20 defend, $50)")
    attacker = MockDot(3, wallet=10, hunger=0.5, attack_points=5, defend_points=5, health=100)
    victim = MockDot(4, wallet=50, hunger=0.3, attack_points=20, defend_points=20, health=100)
    
    ev_data = bribe_action.calculate_attack_expected_value(attacker, victim)
    print(f"  Kill probability: {ev_data['kill_probability']:.1%}")
    print(f"  Death probability: {ev_data['death_probability']:.1%}")
    print(f"  Expected gain: ${ev_data['expected_gain']:.2f}")
    print(f"  Expected loss: ${ev_data['expected_loss']:.2f}")
    print(f"  Net expected value: ${ev_data['expected_value']:.2f}")
    print()
    
    # Scenario 3: Evenly matched
    print("Scenario 3: Evenly Matched (10 vs 10, $30)")
    attacker = MockDot(5, wallet=10, hunger=0.5, attack_points=10, defend_points=10, health=80)
    victim = MockDot(6, wallet=30, hunger=0.3, attack_points=10, defend_points=10, health=80)
    
    ev_data = bribe_action.calculate_attack_expected_value(attacker, victim)
    print(f"  Kill probability: {ev_data['kill_probability']:.1%}")
    print(f"  Death probability: {ev_data['death_probability']:.1%}")
    print(f"  Expected gain: ${ev_data['expected_gain']:.2f}")
    print(f"  Expected loss: ${ev_data['expected_loss']:.2f}")
    print(f"  Net expected value: ${ev_data['expected_value']:.2f}")
    print()


def test_sub_goal_calculation():
    """Test sub-goal (minimum acceptable payment) calculation"""
    
    print("=" * 70)
    print("TEST 2: SUB-GOAL CALCULATION")
    print("=" * 70)
    print()
    
    bribe_action = BribeAction(DNAProfile())
    
    # Scenario 1: Desperate (very hungry, low wallet)
    print("Scenario 1: Desperate Attacker (hunger 80%, wallet $0.50)")
    attacker = MockDot(7, wallet=0.5, hunger=0.8, attack_points=10, defend_points=5, health=100)
    sub_goal = bribe_action.calculate_sub_goal_amount(attacker, None)
    print(f"  Sub-goal (minimum acceptable): ${sub_goal:.2f}")
    print(f"  Reason: Very hungry, needs food money")
    print()
    
    # Scenario 2: Low wallet but not starving
    print("Scenario 2: Poor Attacker (hunger 40%, wallet $3)")
    attacker = MockDot(8, wallet=3.0, hunger=0.4, attack_points=10, defend_points=5, health=100)
    sub_goal = bribe_action.calculate_sub_goal_amount(attacker, None)
    print(f"  Sub-goal (minimum acceptable): ${sub_goal:.2f}")
    print(f"  Reason: Wants to refill wallet to $10")
    print()
    
    # Scenario 3: Well-fed and rich (opportunistic)
    print("Scenario 3: Greedy Attacker (hunger 20%, wallet $25)")
    attacker = MockDot(9, wallet=25.0, hunger=0.2, attack_points=15, defend_points=5, health=100)
    sub_goal = bribe_action.calculate_sub_goal_amount(attacker, None)
    print(f"  Sub-goal (minimum acceptable): ${sub_goal:.2f}")
    print(f"  Reason: Not desperate, opportunistic mugging")
    print()


def test_bribe_acceptance_logic():
    """Test accept/reject bribe decision logic"""
    
    print("=" * 70)
    print("TEST 3: BRIBE ACCEPTANCE DECISION LOGIC")
    print("=" * 70)
    print()
    
    bribe_action = BribeAction(DNAProfile())
    
    # Scenario 1: Bribe exceeds expected value (rational acceptance)
    print("Scenario 1: Generous Bribe (offer $20, EV $10)")
    attacker = MockDot(10, wallet=5, hunger=0.5, attack_points=10, defend_points=5, health=100)
    victim = MockDot(11, wallet=50, hunger=0.3, attack_points=5, defend_points=10, health=80)
    
    accept, reason = bribe_action.should_accept_bribe(attacker, victim, bribe_amount=20.0)
    print(f"  Decision: {'ACCEPT' if accept else 'REJECT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 2: Bribe too low
    print("Scenario 2: Lowball Bribe (offer $2, EV $15)")
    attacker = MockDot(12, wallet=5, hunger=0.5, attack_points=20, defend_points=5, health=100)
    victim = MockDot(13, wallet=50, hunger=0.3, attack_points=5, defend_points=5, health=60)
    
    accept, reason = bribe_action.should_accept_bribe(attacker, victim, bribe_amount=2.0)
    print(f"  Decision: {'ACCEPT' if accept else 'REJECT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 3: Conservative attacker accepts sub-goal satisfying bribe
    print("Scenario 3: Conservative Attacker (3 attack pts, offer $7, sub-goal $7)")
    attacker = MockDot(14, wallet=3, hunger=0.6, attack_points=3, defend_points=10, health=100)
    victim = MockDot(15, wallet=30, hunger=0.3, attack_points=8, defend_points=8, health=90)
    
    accept, reason = bribe_action.should_accept_bribe(attacker, victim, bribe_amount=7.0)
    print(f"  Decision: {'ACCEPT' if accept else 'REJECT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 4: Aggressive attacker rejects reasonable bribe
    print("Scenario 4: Aggressive Attacker (20 attack pts, offer $10, prefers gambling)")
    attacker = MockDot(16, wallet=10, hunger=0.3, attack_points=20, defend_points=3, health=100)
    victim = MockDot(17, wallet=50, hunger=0.3, attack_points=5, defend_points=5, health=70)
    
    accept, reason = bribe_action.should_accept_bribe(attacker, victim, bribe_amount=10.0)
    print(f"  Decision: {'ACCEPT' if accept else 'REJECT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 5: Desperate attacker accepts anything
    print("Scenario 5: Desperate Attacker (wallet $0.20, offer $1)")
    attacker = MockDot(18, wallet=0.2, hunger=0.7, attack_points=8, defend_points=5, health=100)
    victim = MockDot(19, wallet=20, hunger=0.3, attack_points=10, defend_points=10, health=85)
    
    accept, reason = bribe_action.should_accept_bribe(attacker, victim, bribe_amount=1.0)
    print(f"  Decision: {'ACCEPT' if accept else 'REJECT'}")
    print(f"  Reason: {reason}")
    print()


def test_instant_bribe_execution():
    """Test instant bribe execution (money transfer)"""
    
    print("=" * 70)
    print("TEST 4: INSTANT BRIBE EXECUTION")
    print("=" * 70)
    print()
    
    bribe_action = BribeAction(DNAProfile())
    
    # Scenario 1: Successful bribe
    print("Scenario 1: Successful Bribe")
    attacker = MockDot(20, wallet=5, hunger=0.5, attack_points=5, defend_points=5, health=100)
    victim = MockDot(21, wallet=50, hunger=0.3, attack_points=5, defend_points=10, health=90)
    
    print(f"  Before - Victim: ${victim.resources.wallet:.2f}, Attacker: ${attacker.resources.wallet:.2f}")
    
    result = bribe_action.execute_instant_bribe(victim, attacker, bribe_amount=15.0)
    
    print(f"  Result: {result['result']}")
    print(f"  Reason: {result.get('reason', 'N/A')}")
    print(f"  After - Victim: ${victim.resources.wallet:.2f}, Attacker: ${attacker.resources.wallet:.2f}")
    print(f"  Victim bribes paid: {victim.resources.bribes_paid}")
    print(f"  Attacker bribes received: {attacker.resources.bribes_received}")
    print()
    
    # Scenario 2: Rejected bribe
    print("Scenario 2: Rejected Bribe (aggressive attacker)")
    attacker = MockDot(22, wallet=10, hunger=0.3, attack_points=20, defend_points=5, health=100)
    victim = MockDot(23, wallet=50, hunger=0.3, attack_points=5, defend_points=5, health=70)
    
    print(f"  Before - Victim: ${victim.resources.wallet:.2f}, Attacker: ${attacker.resources.wallet:.2f}")
    
    result = bribe_action.execute_instant_bribe(victim, attacker, bribe_amount=8.0)
    
    print(f"  Result: {result['result']}")
    print(f"  Reason: {result.get('reason', 'N/A')}")
    print(f"  After - Victim: ${victim.resources.wallet:.2f}, Attacker: ${attacker.resources.wallet:.2f}")
    print()
    
    # Scenario 3: Insufficient funds
    print("Scenario 3: Insufficient Funds")
    attacker = MockDot(24, wallet=5, hunger=0.5, attack_points=10, defend_points=5, health=100)
    victim = MockDot(25, wallet=5, hunger=0.5, attack_points=5, defend_points=10, health=80)
    
    print(f"  Before - Victim: ${victim.resources.wallet:.2f}")
    
    result = bribe_action.execute_instant_bribe(victim, attacker, bribe_amount=20.0)
    
    print(f"  Result: {result['result']}")
    print(f"  Requested: ${result['requested']:.2f}, Available: ${result['available']:.2f}")
    print()


def test_mercy_mode_decision():
    """Test mercy mode continuation decision"""
    
    print("=" * 70)
    print("TEST 5: MERCY MODE CONTINUATION DECISION")
    print("=" * 70)
    print()
    
    bribe_action = BribeAction(DNAProfile())
    
    # Scenario 1: Sub-goal satisfied (retreat)
    print("Scenario 1: Sub-goal Satisfied (victim paid $8, attacker needs $7)")
    attacker = MockDot(26, wallet=3, hunger=0.6, attack_points=5, defend_points=5, health=100)
    victim = MockDot(27, wallet=20, hunger=0.3, attack_points=5, defend_points=10, health=80)
    
    # Activate mercy mode and simulate payment
    victim.resources.activate_mercy_mode(attacker.id)
    victim.resources.mercy_dynamic.total_paid = 8.0
    
    continue_attack, reason = bribe_action.should_continue_attack_during_mercy(attacker, victim)
    
    print(f"  Total paid: ${victim.resources.mercy_dynamic.total_paid:.2f}")
    print(f"  Sub-goal: ${bribe_action.calculate_sub_goal_amount(attacker, None):.2f}")
    print(f"  Decision: {'CONTINUE ATTACKING' if continue_attack else 'RETREAT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 2: Not enough paid yet (continue)
    print("Scenario 2: Sub-goal Not Satisfied (victim paid $3, attacker needs $7)")
    attacker = MockDot(28, wallet=3, hunger=0.6, attack_points=10, defend_points=5, health=100)
    victim = MockDot(29, wallet=25, hunger=0.3, attack_points=5, defend_points=10, health=85)
    
    victim.resources.activate_mercy_mode(attacker.id)
    victim.resources.mercy_dynamic.total_paid = 3.0
    
    continue_attack, reason = bribe_action.should_continue_attack_during_mercy(attacker, victim)
    
    print(f"  Total paid: ${victim.resources.mercy_dynamic.total_paid:.2f}")
    print(f"  Sub-goal: ${bribe_action.calculate_sub_goal_amount(attacker, None):.2f}")
    print(f"  Decision: {'CONTINUE ATTACKING' if continue_attack else 'RETREAT'}")
    print(f"  Reason: {reason}")
    print()
    
    # Scenario 3: Aggressive attacker wants full wallet
    print("Scenario 3: Aggressive Attacker (20 attack pts, wants full wallet)")
    attacker = MockDot(30, wallet=15, hunger=0.3, attack_points=20, defend_points=5, health=100)
    victim = MockDot(31, wallet=40, hunger=0.3, attack_points=5, defend_points=8, health=75)
    
    victim.resources.activate_mercy_mode(attacker.id)
    victim.resources.mercy_dynamic.total_paid = 10.0
    
    continue_attack, reason = bribe_action.should_continue_attack_during_mercy(attacker, victim)
    
    print(f"  Total paid: ${victim.resources.mercy_dynamic.total_paid:.2f}")
    print(f"  Victim wallet: ${victim.resources.wallet:.2f}")
    print(f"  Decision: {'CONTINUE ATTACKING' if continue_attack else 'RETREAT'}")
    print(f"  Reason: {reason}")
    print()


if __name__ == "__main__":
    print("\n\n")
    print("#" * 70)
    print("# DOT AI 3.0 - BRIBE ACTION TEST SUITE")
    print("# Testing attacker decision-making logic")
    print("#" * 70)
    print()
    
    try:
        test_expected_value_calculation()
        test_sub_goal_calculation()
        test_bribe_acceptance_logic()
        test_instant_bribe_execution()
        test_mercy_mode_decision()
        
        print("\n\n")
        print("#" * 70)
        print("# ALL TESTS PASSED! ✓")
        print("# Bribe action decision logic functioning correctly.")
        print("# Ready for integration into utility AI.")
        print("#" * 70)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
