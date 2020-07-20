# write a problem statement to add 1 at the last index os the array
# and carry out the addition of one with carray in the array 
# and print out the results as a output

'''
a = [9,9,9]
s = ''.join(map(str,a))
print(int(s)+1)
'''

def plus_one(a):
    a[-1] += 1
    for i in reversed(range(1,len(a))):
        if a[i] != 10:
            break
        
        a[i] = 0
        a[i-1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a

print( ''.join( map( str , plus_one([1,4,9]) ) ) ) # printing by mapping

s = (plus_one([9,9,9])) 
s = ''.join(map(str,s))
print(int(s))
