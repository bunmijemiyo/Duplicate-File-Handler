# the following line creates a list from the input, do not modify it, please
prices = [float(price) for price in input().split()]
# prices = [0.75, 1.3, 1, 0.70]
# your code below
print(sorted(prices, reverse=True))