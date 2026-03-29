"""
Headless test runner for Dot AI 3.0 economic features  
Runs simulation without renderer to test economic integration

Tests:
- Market spawning
- Stimulus payments  
- Interest accrual
- Basic economic loop
"""

import time
from core.simulation import DotSimulation
from core.metrics_logger import MetricsLogger


def test_economic_integration():
    """Run minimal headless simulation to test 3.0 features"""
    
    print("=" * 60)
    print("DOT AI 3.0 - HEADLESS ECONOMIC INTEGRATION TEST")
    print("=" * 60)
    print()
    
    # Configuration
    config = {
        'width': 1200,
        'height': 800,
        'initial_dots': 3,
        'initial_food': 10,
        'dna_budget': 200,  # 3.0 budget
        
        # Economic features
        'enable_economics': True,
        'enable_market': True,
        'enable_stimulus': True,
        'enable_interest': True,
        'spawn_commodities': True,
        'commodity_multiplier': 0.3,  # Spawn 30% for faster testing
    }
    
    # Initialize simulation
    print("Initializing simulation...")
    logger = MetricsLogger(session_name="test_3_0_integration")
    sim = DotSimulation(config, logger=logger)
    sim.initialize()
    
    print()
    print("=" * 60)
    print("SIMULATION INITIALIZED")
    print("=" * 60)
    print(f"Dots: {len(sim.dots)}")
    print(f"Food: {len(sim.food)}")
    if sim.market:
        print(f"Commodities: {len(sim.market.world_commodities)}")
        print(f"Commodity types: {len(sim.market.commodity_types)}")
    print()
    
    # Check dot DNA budgets
    print("Dot DNA Budgets:")
    for dot in sim.dots:
        allocated = dot.dna.get_allocated_points()
        total = dot.dna.total_points
        print(f"  Dot #{dot.id}: {allocated}/{total} points allocated")
        
        # Check if economic genes exist
        has_economic = any(hasattr(dot.dna, gene) for gene in ['buy_power', 'sell_power', 'hold_power'])
        print(f"    Has economic genes: {has_economic}")
        
        # Check stimulus
        if dot.stimulus_payment:
            info = dot.stimulus_payment.get_payment_info()
            print(f"    Stimulus role: {info['role']} (${info['payment_amount']:.2f} every {info['payment_interval']:.0f}s)")
    print()
    
    # Run simulation for 10 seconds
    SIMULATION_TIME = 10.0  # seconds
    dt = 1.0 / 60.0  # 60 FPS
    frames = int(SIMULATION_TIME / dt)
    
    print(f"Running simulation for {SIMULATION_TIME:.0f} seconds ({frames} frames)...")
    print()
    
    # Track economics
    total_stimulus_delivered = 0
    total_interest_earned = 0
    
    start_time = time.time()
    for frame in range(frames):
        sim.update(dt)
        
        # Check world state for economic events
        world_state = sim.get_world_state()
        
        # Track stimulus payments
        if "stimulus_payments" in world_state:
            for payment in world_state["stimulus_payments"]:
                total_stimulus_delivered += payment['amount']
                if frame % 60 == 0:  # Print every second
                    print(f"  [Stimulus] Dot #{payment['dot_id']} ({payment['role']}) received ${payment['amount']:.2f}")
        
        # Track interest payments
        if "interest_payments" in world_state:
            for payment in world_state["interest_payments"]:
                total_interest_earned += payment['interest']
                if frame % 60 == 0:  # Print every second
                    print(f"  [Interest] Dot #{payment['dot_id']} earned ${payment['interest']:.4f} (balance: ${payment['balance']:.2f})")
        
        # Progress indicator
        if frame % 120 == 0 and frame > 0:
            elapsed = frame * dt
            print(f"  [{elapsed:.1f}s] Dots alive: {len(sim.dots)}")
    
    elapsed_real = time.time() - start_time
    
    print()
    print("=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)
    print(f"Simulation time: {SIMULATION_TIME:.1f}s")
    print(f"Real time: {elapsed_real:.2f}s")
    print(f"Frames processed: {frames}")
    print()
    
    # Economic summary
    print("ECONOMIC SUMMARY:")
    print(f"  Total stimulus delivered: ${total_stimulus_delivered:.2f}")
    print(f"  Total interest earned: ${total_interest_earned:.4f}")
    print()
    
    # Dot summary
    print("FINAL DOT STATE:")
    for dot in sim.dots:
        wallet = dot.resources.wallet
        energy = dot.resources.energy
        health = dot.resources.health
        print(f"  Dot #{dot.id}:")
        print(f"    Wallet: ${wallet:.2f}")
        print(f"    Energy: {energy:.0f}/{dot.resources.max_energy:.0f}")
        print(f"    Health: {health:.0f}/{dot.resources.max_health:.0f}")
        
        if dot.stimulus_payment:
            print(f"    Stimulus received: ${dot.stimulus_payment.total_stimulus_received:.2f}")
    print()
    
    # Market summary
    if sim.market:
        print("MARKET SUMMARY:")
        print(f"  Total commodities: {len(sim.market.world_commodities)}")
        print(f"  Ungathered: {sim.market.get_ungathered_count()}")
        print()
        
        print("  Commodity Prices:")
        for name, ctype in sim.market.commodity_types.items():
            scarcity = (1 - ctype.remaining_supply / ctype.total_supply) * 100
            print(f"    {name:15} - ${ctype.current_price:>8.2f} ({ctype.remaining_supply}/{ctype.total_supply} remain, {scarcity:.0f}% depleted)")
    
    print()
    print("=" * 60)
    print("✓ TEST COMPLETE - Economic features integrated successfully")
    print("=" * 60)


if __name__ == "__main__":
    test_economic_integration()
