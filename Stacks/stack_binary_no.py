# converting the number into binary number

'''
242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2  = 30  -> 0
30 / 2  = 15  -> 0
15 / 2  = 7   -> 1
7 / 2 = 3     -> 1
3 / 2 = 1     -> 1
1 / 2 = 0	  -> 1
'''
from stacks import Stack

def divide_by_2(num):   
    s = Stack()
    
    if num == 0:
        return 0
    
    while num > 0:      # iterating through the number 
        remainder = num % 2     # taking out the remainder and pushing it into the stack
        s.push(remainder)   
        num = num // 2  # taking out the num for further results
    
    binary_num = ""
    while not s.is_empty():     # iterating the stack up till it is not empty 
        binary_num += str(s.pop())  # and adding it into the binary string
    
    return binary_num
    
print(divide_by_2(242))
print(divide_by_2(997))
print(divide_by_2(999))


    