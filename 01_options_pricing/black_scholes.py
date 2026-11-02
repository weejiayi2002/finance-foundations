import numpy as np
from scipy.stats import norm

"""
THEORY: Black-Scholes Merton Pricing
Calculates the theoretical fair value of a European Call and Put Option
S: Spot Price of the asset
K: Strike Price
T: Time to maturity
r: Risk Free Rate
sigma: Volatility of asset
"""

S = 100.0
K = 100.0
T = 1.0
r = 0.05
sigma = 0.20

d1 = np.log(S / K) + (r + 0.5 * sigma ** 2) * T / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print(f"--- Black-Scholes Pricing ---")
print(f"Call Option Price: ${call_price:.4f}")
print(f"Put Option Price:  ${put_price:.4f}")

"""
Example if market is charging $12.00 for an asset for something mathematically worth $9.97, the option
is overpriced, and you should sell (short) to pocket the overpriced premium rather than buy it, the BS model is your
lie detector against the market (not applicable in real world context as the model assumes constant volatility, where 
in reality volatility is constantly moving
"""
