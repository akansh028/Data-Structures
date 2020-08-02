# Binary searching

# iterative
def binary_iterative(a,element):
    
    first = 0
    last = len(a) -1
    found = False

    while first <= last and not found:
        mid = (first+last)//2
        if a[mid] == element:
            found = True
        else:
            if element < a[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

print(binary_iterative([1,2,3,4,5] , 5))

# recursive

def binary_recursive(a,element):
    if len(a) == 0:
        return False
    else:
        mid = len(a)//2
        if a[mid] == element:
            return True
        else:
            if element < a[mid]:
                return binary_recursive(a[:mid-1], element)
            else:
                return binary_recursive(a[mid+1:], element)

print(binary_recursive([1,2,3,4,5] , 7))