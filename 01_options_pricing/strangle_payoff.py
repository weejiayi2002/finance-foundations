import numpy as np
import matplotlib.pyplot as plt

"""
||THEORY|||
Long Strangle strategy involves buying an Out-of-the-Money Call and an
Out-of-the-Money Put. Both differing in strike prices (K)
Goal: Profit from massive volatility swings while keeping upfront cost lower than Straddle
Risk: The asset must move significantly further to reach a break-even
Maximum Loss: Occurs if stock price stays between the two strike prices
"""
K_put = 95
K_call = 105
put_premium = 2  # Cheaper premium cost due to strike price further away from stock price
call_premium = 2  # Cheaper premium cost due to strike price further away from stock price

S = np.linspace(50, 150, 100)
call_profit = np.maximum(S-K_call, 0) - call_premium
put_profit = np.maximum(K_put-S, 0) - put_premium
strangle_profit = put_profit + call_profit

plt.figure(figsize=(10, 6))
plt.plot(S, call_profit, label="Call Leg", linestyle='--', color='blue', alpha=0.5)
plt.plot(S, put_profit, label='Put Leg', linestyle='--', color='orange', alpha=0.5)
plt.plot(S, strangle_profit, label='Strangle Leg', linestyle="-", color='green', linewidth=3)

plt.axhline(0, color='black', linestyle="--", linewidth=1)  # Horizontal Line
plt.axvline(K_put, color='gray', linestyle=':', label=f'Put Strike Price (K={K_put})')  # Vertical Line
plt.axvline(K_call, color='gray', linestyle=":", label=f'Call Strike Price (K={K_call}')  # Vertical Line
plt.title("Long Strangle Strategy Profit/Loss")
plt.xlabel("Underlying Stock Price at Expiration ($S_T$)")
plt.ylabel("Net Profit / Loss ($)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()