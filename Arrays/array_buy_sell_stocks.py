# in this a array of price of stocks are given at a particular interval 
# of time , we have to return a max profit stock at a particular given time 

def buy_and_sell(a):
    max_profit = 0
    for low in range(len(a)-1):
        for high in range(low+1,len(a)):
            if a[high] - a[low] > max_profit:
                max_profit = a[high] - a[low]
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell(A))