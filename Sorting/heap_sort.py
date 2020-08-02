# program for Max Heap

def heapify(a,n,i):
    largest = i # largest element root
    l = 2*i + 1 # left child 
    r = 2*i + 2 # right child

    if l < n and a[i] < a[l]:   # checking the left child greater than the root
        largest = l
    if r < n and a[largest] < a[r]: # checking the right child greater than the root
        largest = r

    if largest != i:    # if largest element is not root 
        a[i] , a[largest] = a[largest] , a[i]   # swap the root with the largest element
        heapify(a,n,largest)    # again checking 

def heapSort(a):
    n = len(a)  # length of the array
    for i in range(n,-1,-1):    # from end to start
        heapify(a,n,i)  # for each element

    for i in range(n-1 , 0 , -1):   # extraction of the each element 
        a[i] , a[0] = a[0] , a[i]   # swaping to the index element
        heapify(a,i,0)

a = [2,5,3,8,6,5,4,7]
print('unsorted array',a)
heapSort(a)
print('sorted array',a)