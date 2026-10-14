import numpy as np
import matplotlib.pyplot as plt

K = 100       # Strike Price
premium = 5   # Option Premium

# Create array of 100 stock prices from 50 to 150
S = np.linspace(50, 150, 100)   # YOUR CODE HERE

# Payoff functions
# European Call Payoff: max(S - K, 0) - premium
# Rights to buy at lower price (K) and sell at a higher market price --> profit
call_payoff = np.maximum(S - K, 0) - premium

# European Put Payoff: max(K - S, 0) - premium
# Buy at lower market price and rights to sell at higher price (K) --> profit
put_payoff = np.maximum(K - S, 0) - premium

# Plot the payoffs
plt.figure(figsize=(10, 6))
plt.plot(S, call_payoff, label='Long Call Payoff', linewidth=2)
plt.plot(S, put_payoff, label='Long Put Payoff', linewidth=2)

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(K, color='gray', linestyle=':', label=f'Strike Price (K={K})')
plt.title("European Call & Put Option Payoffs at Expiration")
plt.xlabel("Underlying Stock Price at Expiration ($S_T$)")
plt.ylabel("Profit / Loss ($)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()