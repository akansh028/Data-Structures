# print the largest continuos sum in the guven array


def largest_sum(a):
    
    if len(a) == 0:
        return 0
    
    max_sum = current_sum = a[0]
    for num in a[1:]:
        current_sum = max(current_sum+num , num)
        max_sum = max(current_sum , max_sum)
    return max_sum

print(largest_sum([1,2,-1,3,4,10,10,-10,-1]))

