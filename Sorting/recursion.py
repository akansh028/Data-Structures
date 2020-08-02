# Recusion 

#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#multiply
# m + multply(m,n-1)
def multiply(m,n):
    if n == 1:
        return m
    elif m == 1:
        return n
    else:
        return m + multiply(m , n-1)
print(multiply(5,3))