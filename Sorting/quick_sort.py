# quick sort
# using  a pivot element technique
#  low  --> Starting index,  high  --> Ending index from end

def QuickSort(a,left,right):
    if left < right:
        split = partition(a,left,right)

        QuickSort(a,left,split-1)
        QuickSort(a,split+1,right)

def partition(a,left,right):
    
    pivot = a[left] # pivot , first element
    low = left + 1  # first to second element
    high = right    # last element

    while True:
        
        while low <= high and a[low] <= pivot:  # smaller than pivot element
            low += 1
        while low <= high and a[high] >= pivot: # larger than pivot element
            high -= 1   

        if low > high:   # both value high and low which is out of order
            break
        else:
            a[low], a[high] = a[high] , a[low] # swapping the values which is smaller and larger
    
    a[left], a[high] = a[high], a[left]   # moving the pivot to its position
    
    return high


a = [10,7, 8, 9, 1, 5] 
n = len(a)
QuickSort(a, 0 , n-1)
print(a)
