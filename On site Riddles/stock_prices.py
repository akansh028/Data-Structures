# compare the prices of each stocks to get the maximum profit 

def profit(stock_prices):
    
    if len(stock_prices) < 2:
        raise Exception('Need atleast two stock prices')
    
    min_stock_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        comparison_price = price - min_stock_price
        max_profit = max(max_profit, comparison_price)
        min_stock_price = min(min_stock_price,price)
    
    return max_profit

print(profit([25,10,3,10]))
print(profit([25,10,3,1]))
#print(profit([25]))