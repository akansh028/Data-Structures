# find the missing element from the either of the two arrays

import collections

def finder(a1,a2):
    d = collections.defaultdict(int)
    for n in a2:
        d[n] += 1
    for n in a1:
        if d[n] == 0:
            return n
        else:
            d[n] -= 1

a1 = [1,2,3,4,5,6,7]
a2 = [3,7,2,1,4,6]
print(finder(a1,a2))   
 