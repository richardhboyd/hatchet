def maxProfit(k, prices):
    if not prices:
        return 0

    n = len(prices)
    profits = [0]*n
    max_profit = 0

    for i in range(1, k+1):
        prev_profit = 0
        
        for j in range(1, n):
            profit = prices[j] - prices[j-1]
            profits[j] = max(profits[j-1], prev_profit + profit)
            prev_profit = profits[j-1]
        
        max_profit = max(max_profit, profits[-1])
    
    return max_profit
