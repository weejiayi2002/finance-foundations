import numpy as np
import matplotlib.pyplot as plt
"""
Theory: BULL CALL SPREAD
A Bull Call Spread involves buying same amount of Call option
at a lower strike price and selling same amount of Call option at a higher
strike price.
-Goal: To profit from a moderate rise in stock price
-Cost Reduction: Lesser upfront payment, selling of higher-strike price
call option subsidizes the cost of buying the lower-strike call option.
-Risk: Maximum loss ($3), paid $5 for Long Call option and collect $2 from Short Call option
-Reward: Maximum profit ($7), the distance between both strike prices ($110-$100) minus
the $3 to enter the trade. This 3-to-7 ratio is risking $3 to potentially earn $7. 
-Disadvantage: Maximum profits will be capped. Since same amount of Long Call and Short Call,
the gain will be matched by the liability of the short call.
"""

K_long = 100  # Strike price of the Call we BUY
K_short = 110  # Strike price of the Call we SELL
premium_long = 5
premium_short = 2

S = np.linspace(80, 130, 100)
long_call_profit = np.maximum(S - K_long, 0) - premium_long
short_call_profit = -np.maximum(S - K_short, 0) + premium_short  # Cash outflow if stock price > strike price
spread_profit = long_call_profit + short_call_profit

plt.figure(figsize=(10, 6))
plt.plot(S,long_call_profit, label='Long Call Leg', linestyle='--', color='blue', alpha=0.5)
plt.plot(S, short_call_profit, label='Short Call Leg', linestyle='--',color='red', alpha=0.5)
plt.plot(S, spread_profit, label='Combined Spread Profit', linestyle="-", color='green', linewidth=3)

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(K_long, color='gray',linestyle=':', label=f'Long Strike (K={K_long})')
plt.axvline(K_short, color='gray', linestyle=":", label=f'Short Strike (K={K_short})')
plt.title('Bull Call Spread Profit/Loss')
plt.xlabel('Underlying Stock Price at Expiration ($S_T$)')
plt.ylabel('Net Profit / Loss ($)')
plt.legend()
plt.show()