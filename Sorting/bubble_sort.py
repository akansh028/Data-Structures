# bubble sort

def bubble(a):
    for i in range(len(a)-1, 0 , -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubble([5,3,7,2]))