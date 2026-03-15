"""
Stimulus Payment System (Universal Basic Income)
Dot AI 3.0 - Periodic cash payments for living dots

This creates continuous money supply growth and tests:
- Does free money reduce violence?
- Does it create inflation?
- Do different payment rates affect role selection?
"""

import time


class StimulusPayment:
    """
    Universal Basic Income system for dots
    
    Dots receive periodic cash payments for being alive.
    Payment rate depends on their economic role (DNA-based).
    
    Why this exists:
    - Prevents bankruptcy-driven starvation
    - Creates ongoing money supply growth (inflation test)
    - Tests monetary policy impact on violence rates
    - Rewards different economic strategies differently
    """
    
    def __init__(self, dot):
        """
        Initialize stimulus payment tracker for a dot
        
        Args:
            dot: The dot receiving payments
        """
        self.dot = dot
        self.last_payment_time = time.time()
        
        # Payment tracking
        self.total_stimulus_received = 0.0
        self.payment_count = 0
        
        # Role-based payment schedule (determined from DNA)
        self.role, self.payment_amount, self.payment_interval = self._determine_payment_schedule()
    
    def _determine_payment_schedule(self):
        """
        Determine stimulus payment schedule based on dot's economic role
        
        Role classification based on DNA gene distribution:
        - TRADER: High buy_power + sell_power → Small frequent payments
        - INVESTOR: High hold_power + max_wallet → Large infrequent payments
        - GENERALIST: Balanced genes → Moderate payments
        - NON-ECONOMIC: No economic genes → Basic survival payments
        
        Returns:
            (role_name, payment_amount, interval_seconds)
        """
        dna = self.dot.dna
        
        # Calculate specialization scores
        trader_score = 0
        if hasattr(dna, 'buy_power'):
            trader_score += dna.buy_power.points if dna.buy_power.enabled else 0
        if hasattr(dna, 'sell_power'):
            trader_score += dna.sell_power.points if dna.sell_power.enabled else 0
        if hasattr(dna, 'market_visibility'):
            trader_score += dna.market_visibility.points if dna.market_visibility.enabled else 0
        
        investor_score = 0
        if hasattr(dna, 'hold_power'):
            investor_score += dna.hold_power.points if dna.hold_power.enabled else 0
        if hasattr(dna, 'max_wallet'):
            investor_score += dna.max_wallet.points if dna.max_wallet.enabled else 0
        
        gatherer_score = 0
        if hasattr(dna, 'gather_speed'):
            gatherer_score += dna.gather_speed.points if dna.gather_speed.enabled else 0
        
        # Determine role and payment schedule
        if trader_score >= 40:
            # TRADER: Small frequent payments (active trading cashflow)
            return "TRADER", 0.10, 20.0  # $0.10 every 20 seconds
        
        elif investor_score >= 40:
            # INVESTOR: Large infrequent payments (passive investment income)
            return "INVESTOR", 0.50, 100.0  # $0.50 every 100 seconds
        
        elif gatherer_score >= 30:
            # GATHERER: Moderate payments (resource collection bonus)
            return "GATHERER", 0.15, 30.0  # $0.15 every 30 seconds
        
        elif trader_score + investor_score + gatherer_score >= 20:
            # GENERALIST: Balanced payments
            return "GENERALIST", 0.20, 40.0  # $0.20 every 40 seconds
        
        else:
            # NON-ECONOMIC: Basic survival UBI
            return "NON-ECONOMIC", 0.05, 30.0  # $0.05 every 30 seconds
    
    def check_payment(self, current_time):
        """
        Check if payment is due and deliver if ready
        
        Args:
            current_time: Current simulation time (seconds since epoch)
        
        Returns:
            dict with payment result:
            - result: 'PAYMENT_DELIVERED', 'NOT_DUE', or 'WALLET_FULL'
            - amount: Payment amount if delivered
            - new_balance: Wallet balance after payment
        """
        time_since_last = current_time - self.last_payment_time
        
        # Check if payment interval has elapsed
        if time_since_last < self.payment_interval:
            return {
                'result': 'NOT_DUE',
                'time_remaining': self.payment_interval - time_since_last
            }
        
        # Check if wallet has space
        if self.dot.resources.wallet >= self.dot.resources.max_wallet:
            return {
                'result': 'WALLET_FULL',
                'wallet': self.dot.resources.wallet,
                'max_wallet': self.dot.resources.max_wallet
            }
        
        # Deliver payment (capped at wallet max)
        space_available = self.dot.resources.max_wallet - self.dot.resources.wallet
        actual_payment = min(self.payment_amount, space_available)
        
        self.dot.resources.wallet += actual_payment
        self.last_payment_time = current_time
        self.total_stimulus_received += actual_payment
        self.payment_count += 1
        
        return {
            'result': 'PAYMENT_DELIVERED',
            'amount': actual_payment,
            'new_balance': self.dot.resources.wallet,
            'total_received': self.total_stimulus_received,
            'payment_number': self.payment_count
        }
    
    def get_payment_info(self):
        """
        Get information about this dot's stimulus payment schedule
        
        Returns:
            dict with payment details
        """
        return {
            'role': self.role,
            'payment_amount': self.payment_amount,
            'payment_interval': self.payment_interval,
            'payments_per_minute': 60.0 / self.payment_interval,
            'income_per_minute': (60.0 / self.payment_interval) * self.payment_amount,
            'total_received': self.total_stimulus_received,
            'payment_count': self.payment_count
        }
    
    def get_stats(self):
        """
        Get stimulus payment statistics for this dot
        
        Returns:
            dict with lifetime payment stats
        """
        elapsed = time.time() - self.last_payment_time
        
        return {
            'role': self.role,
            'total_stimulus': self.total_stimulus_received,
            'payment_count': self.payment_count,
            'average_payment': self.total_stimulus_received / max(1, self.payment_count),
            'time_since_last': elapsed,
            'next_payment_in': max(0, self.payment_interval - elapsed)
        }


class StimulusSystem:
    """
    Global stimulus payment manager for simulation
    
    Tracks total money supply injected into economy via UBI.
    Used for economic analysis and inflation tracking.
    """
    
    def __init__(self):
        """Initialize global stimulus tracking"""
        self.total_stimulus_paid = 0.0
        self.total_payments = 0
        self.payments_by_role = {
            'TRADER': {'amount': 0.0, 'count': 0},
            'INVESTOR': {'amount': 0.0, 'count': 0},
            'GATHERER': {'amount': 0.0, 'count': 0},
            'GENERALIST': {'amount': 0.0, 'count': 0},
            'NON-ECONOMIC': {'amount': 0.0, 'count': 0}
        }
    
    def record_payment(self, role, amount):
        """
        Record a stimulus payment in global statistics
        
        Args:
            role: Economic role receiving payment
            amount: Payment amount
        """
        self.total_stimulus_paid += amount
        self.total_payments += 1
        
        if role in self.payments_by_role:
            self.payments_by_role[role]['amount'] += amount
            self.payments_by_role[role]['count'] += 1
    
    def get_money_supply_growth(self):
        """
        Get total money injected into economy via stimulus
        
        Returns:
            Total stimulus payments delivered
        """
        return self.total_stimulus_paid
    
    def get_payment_breakdown(self):
        """
        Get stimulus payment breakdown by economic role
        
        Returns:
            dict with per-role statistics
        """
        breakdown = {}
        
        for role, data in self.payments_by_role.items():
            if data['count'] > 0:
                breakdown[role] = {
                    'total_paid': data['amount'],
                    'payment_count': data['count'],
                    'average_payment': data['amount'] / data['count'],
                    'percent_of_total': (data['amount'] / self.total_stimulus_paid * 100) if self.total_stimulus_paid > 0 else 0
                }
        
        return breakdown
    
    def get_stats(self):
        """
        Get comprehensive stimulus system statistics
        
        Returns:
            dict with global stimulus data
        """
        return {
            'total_stimulus_paid': self.total_stimulus_paid,
            'total_payments': self.total_payments,
            'average_payment': self.total_stimulus_paid / max(1, self.total_payments),
            'payments_by_role': self.get_payment_breakdown()
        }
