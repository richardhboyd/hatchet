def maxProfit(prices):
    firstBuy = float('inf')
    firstSell = 0
    secondBuy = float('inf')
    secondSell = 0
    
    for price in prices:
        firstBuy = min(firstBuy, price)
        firstSell = max(firstSell, price - firstBuy) 
        secondBuy = min(secondBuy, price - firstSell)
        secondSell = max(secondSell, price - secondBuy)
        
    return secondSell
