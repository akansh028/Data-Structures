# Sequential search

def seq(a,element):

    pos = 0
    found = False
    stopped = False

    while pos < len(a) and not found and not stopped:
        if a[pos] == element:
            found = True
        else:
            if a[pos] > element:
                stopped = True
            else:
                pos += 1
    return found

print(seq([1,2,3,4,5] , 1))