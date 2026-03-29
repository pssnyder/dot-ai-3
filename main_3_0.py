"""
=====================================================================
🧬 DOT AI 3.0: THE HYBRID COMBAT-ECONOMIC SIMULATOR 🌍💰
=====================================================================

EVOLUTION: Dot AI 2.0 (Combat/Survival) → Dot AI 3.0 (Economics)

NEW IN 3.0:
- 📊 Market System: Finite resources with scarcity pricing
- 💰 Economic Actions: Gather, Buy, Sell, Consume
- 🏦 Stimulus Payments: Universal Basic Income (UBI)
- 📈 Interest System: Passive income for investors
- 🤝 Mercy Dynamic: Wallet trickle bribery
- 🧬 Economic DNA: 6 new genes (buy_power, sell_power, etc.)

THE EXPERIMENT:
Will dots choose peaceful commerce or violent theft when:
- Resources are finite (no respawn)
- Wallets are lootable (kill → steal money)
- Stimulus creates inflation
- Interest rewards capital accumulation

=====================================================================
"""

from datetime import datetime
from core.simulation import DotSimulation
from core.metrics_logger import MetricsLogger
from renderers.pygame_renderer import PygameRenderer


def main():
    """
    Main entry point for Dot AI 3.0 simulation.
    """
    
    print("=" * 60)
    print("🧬 DOT AI 3.0 - HYBRID COMBAT-ECONOMIC SIMULATOR")
    print("=" * 60)
    print("Combat + Trading + Finite Resources + Market Economy")
    print("")
    
    # ===== CONFIGURATION =====
    config = {
        # World settings
        'width': 3200,
        'height': 1200,
        
        # Population settings
        'initial_dots': 8,       # Reduced for economic testing
        'initial_food': 30,      # Reduced - dots should trade more
        
        # DNA settings (3.0)
        'dna_budget': 200,       # Increased from 100 to allow economic genes
        
        # Economic settings (3.0)
        'enable_economics': True,  # Toggle economic features
        'enable_market': True,     # Enable commodity market
        'enable_stimulus': True,   # Enable UBI payments
        'enable_interest': True,   # Enable passive income
        
        # Market settings (3.0)
        'spawn_commodities': True,
        'commodity_multiplier': 0.5,  # Spawn 50% of normal commodities (scarcity test)
    }
    
    # Initialize metrics logger
    session_name = datetime.now().strftime("%Y%m%d_%H%M%S") + "_v3.0"
    print(f"📊 Starting logging session: {session_name}")
    logger = MetricsLogger(session_name=session_name)
    
    # Initialize simulation
    print("⚙️  Initializing Dot AI 3.0 simulation...")
    simulation = DotSimulation(config, logger=logger)
    simulation.initialize()
    
    # Initialize renderer
    print("🎨 Initializing renderer...")
    renderer = PygameRenderer(config['width'], config['height'])
    
    print("")
    print("✅ READY!")
    print("")
    print("CONTROLS:")
    print("  SPACE - Pause/Resume")
    print("  ESC   - Quit")
    print("")
    print("WATCH FOR:")
    print("  💰 Economic transactions (buy, sell, gather)")
    print("  🏦 Stimulus payments (UBI)")
    print("  📈 Interest earnings (passive income)")
    print("  🤝 Mercy Dynamic (wallet trickle)")
    print("  ⚔️  Combat (wallet looting)")
    print("")
    print("=" * 60)
    print("")
    
    # Main loop
    running = True
    while running:
        # Handle input
        event = renderer.handle_events()
        
        if event == "quit":
            running = False
        elif event == "pause":
            simulation.toggle_pause()
        
        # Update simulation (logic)
        delta_time = 1.0 / 60.0
        simulation.update(delta_time)
        
        # Render (visuals)
        state = simulation.get_state()
        actual_delta = renderer.render(state)
    
    # Cleanup
    print("\n👋 Shutting down...")
    print("📊 Metrics saved to:", logger.get_log_path())
    renderer.quit()
    print("✅ Done!")


if __name__ == "__main__":
    main()
