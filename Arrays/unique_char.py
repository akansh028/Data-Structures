# if string is unique char or not

def unique(s):
    return len(set(s)) == len(s)

print(unique('abcdee'))

            # -------OR----------#

def unique2(s):
    char = set()
    for i in s:
        if i in char:
            return False
        else:
            char.add(i)
    return True
print(unique2('abcdee')) 