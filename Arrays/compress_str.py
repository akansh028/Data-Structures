# compress the string to form better memory utilization

def compress(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + '1'
    count = 1
    i = 1

    string = ''
    while i < len(s):
        if s[i] == s[i-1]:
            count += 1
        else:
            string += s[i-1] + str(count)
            count = 1
        i += 1
    return  string + s[i-1] + str(count)    # for final concatenation

print(compress('AABCCCDDE'))