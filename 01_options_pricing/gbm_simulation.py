import numpy as np
import matplotlib.pyplot as plt
"""
THEORY: Geometric Brownian Motion (GBM)
Simulating of continuous-time stock price paths using
random normal shocks.
- Drift (mu): The general upward trend of the market
- Volatility (sigma): The intensity of the random shocks
- dz: The Wiener process random variable
"""

S0 = 100.0
mu = 0.08  # Expected annual return
sigma = 0.20  # Annual volatility
T = 1.0  # 1-year
N = 252
dt = T / N  # Length of each time step
paths = 10  # Total number of random paths

# Create matrix
S = np.zeros((N + 1, paths))  # Includes starting point (1) and 252 trading steps
S[0] = S0  # Day 0 (row 0) of all paths set to initial stock price

# Generate random shocks
np.random.seed(42)
Z = np.random.standard_normal((N, paths))  # Passing tuple to size parameter, makes matrix
# Size is (N, paths) as shocks occur only on trading days (eg, Day 0 to day 1, Day 1 to Day 2...)


# Price Path Simulation
for t in range(1, N+1):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[t-1])

plt.figure(figsize=(10, 6))
plt.plot(S, linewidth=1, alpha=0.8)
plt.title("Geometric Brownian Motion: 10 Simulated Stock Paths")
plt.xlabel("Trading Days")
plt.ylabel("Stock Price ($)")
plt.axhline(S0, color='black', linestyle='--', linewidth=1)
plt.grid(True, alpha=0.3)
plt.show()


