#sell at the smallest minimum cost price last seen

def stockOnce(arr):
    min_cost = arr[0]
    max_profit = -float("inf")
    for price in arr:
        #get last_seen minimum cost
        min_cost = min(min_cost, price)
        #get profit
        profit = price - min_cost
        #keep track of max profit
        max_profit = max( max_profit, profit)


    return max_profit

print(stockOnce([310,315,275,295,260,270,290,230,255,250]))