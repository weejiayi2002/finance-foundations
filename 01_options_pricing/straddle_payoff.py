import numpy as np
import matplotlib.pyplot as plt

"""
||Theory|| 
Long Straddle is not a bet on which way a stock will got but on its volatility. Having both
Call and Put options at the same Strike Price (K)
Goal: Profits from major price volatility (price swings MASSIVELY in either directions)
Risk: High premium paid as buying two contracts
Max Loss: When stock price stays exactly at K
"""

K = 100
call_premium = 5
put_premium = 4

S = np.linspace(50, 150, 100)
call_profit = np.maximum(S - K, 0) - call_premium  # Recall, any negative value of 'S-K' is changed to 0
put_profit = np.maximum(K - S, 0) - put_premium
straddle_profit = call_profit + put_profit  # Holding both Call and Put simultaneously

plt.figure(figsize=(10, 6))
plt.plot(S, call_profit, label='Call Leg', linestyle='--', color='blue', alpha=0.5)
plt.plot(S, put_profit, label='Put Leg', linestyle='--', color='orange', alpha=0.5)
plt.plot(S, straddle_profit, label='Straddle Leg', linestyle='-', color='purple', linewidth=3)

plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Labelling of break even line
plt.axvline(K, color='gray', linestyle=':', label=f'Strike Price (K={K})')  # Labelling of Strike Price (maximum loss)
plt.title("Long Straddle Strategy Profit/Loss")
plt.xlabel("Underlying Stock Price at Expiration ($S_T$)")
plt.ylabel("Net Profit / Loss ($)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
