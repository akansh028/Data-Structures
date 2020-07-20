# write a program to write the pointer can reach furthermost in an array

def array_advance(a):
    i = 0
    last = len(a) - 1
    reach = 0

    while i <= reach and reach < last:
        reach = max(reach , a[i]+i)
        i+=1
    return reach >= last
a = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(a))

A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))