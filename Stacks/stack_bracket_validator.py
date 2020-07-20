from stacks import Stack # imported pre created module stack

def is_match(p1, p2):  # matching the first and the last bracket
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False    # if not matched returning false 

def parenthesis_balanced(string):   # function to check the balance of the bracket
    s = Stack() # initializing the stack
    i = 0   # first index 
    balanced = True     
    while i < len(string) and balanced:     # going through all the brackets
        paren = string[i]   
        if paren in '({[':  # checking is starting brackets are these or not if true then pushing into the stack
            s.push(paren)
        else:
            if s.is_empty():        
                balanced = False
            else:
                top = s.pop()       # pop the last bracket 
                if not is_match(top , paren):   # and calling the function for the validity 
                    balanced = False
        i += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


print(parenthesis_balanced("(((({}))))"))
print(parenthesis_balanced("[][]]]"))
print(parenthesis_balanced("[][]"))
