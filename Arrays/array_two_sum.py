# Given an array of integers, return the two numbers such that they add up to
# a specific target. You may assume that each input would have exactly one
# solution, and you may not use the same element twice.

def two_sum(a , target):
    i = 0
    j = len(a) - 1
    
    while i < j:
        if a[i] + a[j] == target:
            print(a[i],a[j])
            return True
        elif a[i] + a[j] < target:
            i += 1
        else:
            j -= 1
    return False


a = [5,3,8,6,2,9,4,1,6,7]
print(two_sum(a,7))
