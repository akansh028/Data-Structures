# using stack module we need to reverse a string 

'''
s = 'HelloWorld'
print(s[::-1])
'''

from stacks import Stack

def reverse_str(string):
    s = Stack()
    
    for i in range(len(string)):
        s.push(string[i])
    
    reverse_string = ""

    while not s.is_empty():
        reverse_string += s.pop()
    
    return reverse_string

print(reverse_str('HelloWorld'))


