'''Euclids Algorithm - Algo to find the max gcd 
    gcd (m,n) = gcd (n , m-n)
'''
# Method 1

def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    if m%n == 0:
        return n
    else:
        diff = m-n
        return gcd(max(n,diff) , min(m,diff))

gcd_first = gcd(98,56)
print(gcd_first)

# Method 2

def gcd1(m,n):
    if m < n:
        (m,n) = (n,m)
    if m%n == 0:
        return n 
    else:
        return gcd1(n , m%n)
gcd_second = gcd1(98,56)
print(gcd_second)

