# merge sort
# using technique divide and conquer

def MergeSort(A,B): #two lists
    (c,m,n) = ([] , len(A) , len(B))
    (i,j) = (0,0) #starting indexes of both the lists 
    while i+j < m+n:  # index of the sum of the lists is less than the lengths of the lists
        
        if i == m: # A is blank
            c.append(B[j])            
            j+=1
        elif j == n: # B is blank
            c.append(A[i])
            i+=1
        elif A[i] < B[j]: # element of A is less than B
            c.append(A[i])
            i+=1
        else:              # element of B is less than A
            c.append(B[j])
            j+=1
    return c

a = list(range(0,100,2))
b = list(range(1,110,3))
print(MergeSort(a,b))