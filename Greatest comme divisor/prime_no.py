from math import *

def isprime(n):
    prime_list = []
    for num in range(1,n+1):
        if num > 1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                prime_list += [num]
    return prime_list

prime_numbers = isprime(99)
print(prime_numbers)
