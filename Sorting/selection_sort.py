# selection sort

def SelectionSort(l):
    for start in range(len(l)):      
        for i in range(start , len(l)):
            first_pos = start
            if l[i] < l[first_pos]:
                first_pos = i
                (l[start] , l[first_pos]) = (l[first_pos] , l[start])
    return l

print(SelectionSort([5,3,9,7,2,1,8,4,6]))

