import numpy as np

prices = np.array([100.0, 102.5, 99.0, 105.0, 101.2])

new_prices = prices * 1.05

weights = np.array([0.2, 0.3, 0.1, 0.25, 0.15])

portfolio_value = np.dot(new_prices, weights)

print("Original Prices:", prices)
print("Dimensions:", prices.shape)
print("New Prices:", new_prices)
print("Portfolio Value:", portfolio_value)