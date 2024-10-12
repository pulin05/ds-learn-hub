import numpy as np
import matplotlib.pyplot as plt

# Example stock price data (replace with real data)
stock_prices = np.array([120, 125, 130, 128, 132, 135, 138, 140])

# Normalize stock prices
P_min = np.min(stock_prices)
P_max = np.max(stock_prices)
normalized_prices = (stock_prices - P_min) / (P_max - P_min)

# Logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Apply logistic map
r = 3.57  # Chaotic region
steps = 100  # Number of steps
logistic_prices = [normalized_prices[0]]

for _ in range(steps - 1):
    logistic_prices.append(logistic_map(logistic_prices[-1], r))

# Denormalize back to stock prices
logistic_prices = np.array(logistic_prices)
print(logistic_prices)
denormalized_prices = logistic_prices * (P_max - P_min) + P_min

# Plot the result
# plt.plot(denormalized_prices)
# plt.title("Stock Prices Modeled by Logistic Map")
# plt.xlabel("Time Steps")
# plt.ylabel("Price")
# plt.show()
