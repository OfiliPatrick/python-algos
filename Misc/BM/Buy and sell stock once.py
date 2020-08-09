def buyAndSell1(prices):
    min_cp = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        price = prices[i]

        min_cp = min(min_cp, price)

        profit = price - min_cp

        max_profit = max(max_profit, profit)
        

    return max_profit


print(buyAndSell1([7, 1, 5, 3, 6, 4]))
print(buyAndSell1([7, 6,4,3,1]))