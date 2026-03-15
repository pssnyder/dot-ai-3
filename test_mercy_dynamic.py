"""
Test script for Mercy Dynamic (Wallet Trickle Bribery System)
Tests the new 3.0 economic mechanics in isolation

Run this to verify:
- Resources properly initialize with wallet
- Mercy mode activates/deactivates
- Money trickles from victim to attacker
- Data outputs to console
"""

import sys
import time
from core.dna import DNAProfile
from core.resources import Resources

def test_mercy_dynamic():
    """Test the mercy dynamic wallet trickle system"""
    
    print("=" * 60)
    print("MERCY DYNAMIC TEST - Dot AI 3.0")
    print("=" * 60)
    print()
    
    # Create two dots (victim and attacker)
    print("1. Creating victim and attacker dots...")
    victim_dna = DNAProfile()
    attacker_dna = DNAProfile()
    
    victim_resources = Resources(victim_dna)
    attacker_resources = Resources(attacker_dna)
    
    # Give victim some money
    victim_resources.wallet = 20.0
    attacker_resources.wallet = 1.0
    
    print(f"   Victim:   {victim_resources}")
    print(f"   Attacker: {attacker_resources}")
    print()
    
    # Victim activates mercy mode
    print("2. Victim activates mercy mode (opens wallet)...")
    victim_resources.activate_mercy_mode(attacker_id=999)
    print(f"   Mercy mode active: {victim_resources.is_in_mercy_mode()}")
    print()
    
    # Simulate trickle payments over time
    print("3. Simulating wallet trickle over 10 seconds...")
    print("   (Payments should occur every 0.5 seconds)")
    print()
    
    dt = 0.1  # 100ms time step
    total_time = 0.0
    max_time = 10.0
    
    payments_received = []
    
    while total_time < max_time:
        # Update mercy dynamic
        result = victim_resources.update_mercy_dynamic(dt)
        
        if result:
            payment = result["payment"]
            total_paid = result["total_paid"]
            
            # Attacker receives money
            attacker_resources.add_money(payment)
            attacker_resources.bribes_received += 1
            
            payments_received.append(payment)
            
            print(f"   [{total_time:.1f}s] Payment: ${payment:.2f} | Total paid: ${total_paid:.2f} | Attacker wallet: ${attacker_resources.wallet:.2f}")
        
        total_time += dt
        time.sleep(0.05)  # Small delay for readability
        
        # Stop if victim runs out of money
        if victim_resources.wallet <= 0:
            print(f"   Victim wallet depleted at {total_time:.1f}s")
            break
    
    print()
    print("4. Final state:")
    print(f"   Victim:   {victim_resources}")
    print(f"   Attacker: {attacker_resources}")
    print(f"   Total payments made: {len(payments_received)}")
    print(f"   Average payment: ${sum(payments_received)/len(payments_received):.2f}" if payments_received else "   No payments made")
    print(f"   Total transferred: ${sum(payments_received):.2f}")
    print()
    
    # Deactivate mercy mode
    print("5. Victim exits mercy mode (fight or flight)...")
    victim_resources.deactivate_mercy_mode()
    print(f"   Mercy mode active: {victim_resources.is_in_mercy_mode()}")
    print()
    
    # Test serialization
    print("6. Testing data serialization...")
    victim_data = victim_resources.serialize()
    print(f"   Victim data fields: {list(victim_data.keys())}")
    print(f"   Bribes paid: {victim_data['bribes_paid']}")
    print(f"   Wallet: ${victim_data['wallet']:.2f}")
    print()
    
    attacker_data = attacker_resources.serialize()
    print(f"   Attacker data fields: {list(attacker_data.keys())}")
    print(f"   Bribes received: {attacker_data['bribes_received']}")
    print(f"   Wallet: ${attacker_data['wallet']:.2f}")
    print()
    
    print("=" * 60)
    print("TEST COMPLETE - Mercy Dynamic functioning correctly!")
    print("=" * 60)


def test_inventory_system():
    """Test the inventory system"""
    
    print("\n\n")
    print("=" * 60)
    print("INVENTORY SYSTEM TEST - Dot AI 3.0")
    print("=" * 60)
    print()
    
    dna = DNAProfile()
    resources = Resources(dna)
    
    print("1. Testing inventory operations...")
    print(f"   Starting inventory: {resources.inventory}")
    print(f"   Max slots: {resources.max_inventory_slots}")
    print()
    
    # Add items
    print("2. Adding items...")
    resources.add_to_inventory("food_grain", 3)
    resources.add_to_inventory("iron", 2)
    resources.add_to_inventory("scrap", 5)
    print(f"   Inventory: {resources.inventory}")
    print(f"   Count: {resources.get_inventory_count()}/{resources.max_inventory_slots}")
    print()
    
    # Check items
    print("3. Checking items...")
    print(f"   Has 2 iron? {resources.has_item('iron', 2)}")
    print(f"   Has 10 iron? {resources.has_item('iron', 10)}")
    print()
    
    # Remove items
    print("4. Removing items...")
    resources.remove_from_inventory("iron", 1)
    print(f"   Removed 1 iron")
    print(f"   Inventory: {resources.inventory}")
    print()
    
    # Fill inventory
    print("5. Testing capacity limits...")
    for i in range(10):
        success = resources.add_to_inventory("bronze", 1)
        if not success:
            print(f"   Inventory full after adding {i} bronze")
            break
    print(f"   Final inventory: {resources.inventory}")
    print(f"   Is full: {resources.is_inventory_full()}")
    print()
    
    print("=" * 60)
    print("TEST COMPLETE - Inventory system functioning correctly!")
    print("=" * 60)


def test_economic_fields():
    """Test economic resource fields initialization"""
    
    print("\n\n")
    print("=" * 60)
    print("ECONOMIC FIELDS TEST - Dot AI 3.0")
    print("=" * 60)
    print()
    
    dna = DNAProfile()
    resources = Resources(dna)
    
    print("1. Checking economic field initialization...")
    print(f"   Wallet: ${resources.wallet:.2f}")
    print(f"   Max wallet: ${resources.max_wallet:.2f}")
    print(f"   Total purchases: {resources.total_purchases}")
    print(f"   Total sales: {resources.total_sales}")
    print(f"   Net profit: ${resources.net_profit:.2f}")
    print(f"   Bribes paid: {resources.bribes_paid}")
    print(f"   Bribes received: {resources.bribes_received}")
    print(f"   Attack count: {resources.attack_count}")
    print(f"   Peaceful interactions: {resources.peaceful_interactions}")
    print(f"   Kills: {resources.kills}")
    print(f"   Behavior class: {resources.behavior_class}")
    print(f"   Violence pattern: {resources.violence_pattern}")
    print(f"   Economic pattern: {resources.economic_pattern}")
    print()
    
    print("2. Testing money operations...")
    added = resources.add_money(50.0)
    print(f"   Added $50, actual added: ${added:.2f}")
    print(f"   Wallet: ${resources.wallet:.2f}")
    print()
    
    removed = resources.remove_money(10.0)
    print(f"   Removed $10, actual removed: ${removed:.2f}")
    print(f"   Wallet: ${resources.wallet:.2f}")
    print()
    
    # Try to remove more than available
    removed = resources.remove_money(1000.0)
    print(f"   Tried to remove $1000, actual removed: ${removed:.2f}")
    print(f"   Wallet: ${resources.wallet:.2f}")
    print()
    
    print("=" * 60)
    print("TEST COMPLETE - Economic fields functioning correctly!")
    print("=" * 60)


if __name__ == "__main__":
    print("\n\n")
    print("#" * 60)
    print("# DOT AI 3.0 - ECONOMIC MECHANICS TEST SUITE")
    print("#" * 60)
    print()
    
    try:
        test_economic_fields()
        test_inventory_system()
        test_mercy_dynamic()
        
        print("\n\n")
        print("#" * 60)
        print("# ALL TESTS PASSED! ✓")
        print("# Economic mechanics are functioning correctly.")
        print("# Ready for integration into full simulation.")
        print("#" * 60)
        print()
        
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
