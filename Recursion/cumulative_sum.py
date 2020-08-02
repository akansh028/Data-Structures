# print tghe cumulatie sum of the number
# if n=4, return 10

# example - 4+3+2+1+0 = 10

def cum_sum(n):
    if n == 0:
        return 0
    else:
        return n + cum_sum(n-1)

print(cum_sum(1))