# Write a function or return a list in which for each index the element will be the product of all the
# integers except for the element at the index.

def prod_list(l):
    output = [None] * len(l)
    product = 1
    i = 0

    while i < len(l):       # traversing from front 
        output[i] = product # initializing the output 
        product *= l[i]     # product with the list 
        i += 1
        #print(output,product)
    product = 1
    i = len(l) -1

    while i >= 0:           # traversing from last
        output[i] *= product    
        product *= l[i]
        i -= 1
    
    return output

print(prod_list([1,2,3,4,5]))
    