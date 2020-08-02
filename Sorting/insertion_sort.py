# insertion sort 

def InsertionSort(l):
    for i in range(len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

print(InsertionSort([5,3,9,7,2,1,8,4,6]))