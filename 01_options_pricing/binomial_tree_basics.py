import numpy as np
"""
THEORY: One-step Binomial Tree (European Call)
- Stock moves Up (S * u) or Down (S * d) be a factor {u, d}
- Find the option payoff in the Up or Down state
- Discount the expected payoff back to today
"""

# Parameters
S0 = 100.0
K = 105.0
T = 1.0  # Time to expiration in years
r = 0.05  # Risk-free interest rate
u = 1.2  # Upwards movement factor (20% increase)
d = 0.8  # Downwards movement factor (20% decrease)

# Calculation of risk-neutral probability (p)
# Formula: p = (exp(r * T) - d) / (u - d)
p = (np.exp(r * T) - d) / (u - d)

# Possible future stock prices
S_up = S0 * u
S_down = S0 * d

# Call PAYOFFS in both future states
C_up = np.maximum(S_up - K, 0)
C_down = np.maximum(K - S_down, 0)

# Today's option price (C0)
C0 = np.exp(-r * T) * (p * C_up + (1-p) * C_down)
# Expectation value of future prices discounted to today's price
# by using continuous compounding (np.exp)

print(f"Risk-Neutral Probability (p): {p:.4f}")
print(f"Call Option Value Today (C0): {C0:.4f}")