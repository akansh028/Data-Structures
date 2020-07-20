#gcd - maximum commen divisor

def gcd(m,n):
    commen_factor = []
    for i in range(1 , min(m,n)+1):
        if m%i==0 and n%i==0:
            commen_factor.append(i)
    return(commen_factor[-1])

greatest_commen_divisor = gcd(64,8)
print(greatest_commen_divisor)
