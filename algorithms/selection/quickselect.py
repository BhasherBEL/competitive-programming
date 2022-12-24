import random

def quickmedian(arr):
    return quickselect(arr, (len(arr)+1)//2)


def quickselect(arr, k, l=0, r=None):
    if r is None:
        r = len(arr)-1

    while l <= r:
        p = partition(arr, l, r)
        
        if p == k-1:
            return p, arr[p]
        if p > k-1:
            r = p-1
        else:
            l = p+1

    return -1, -1


def partition(arr, l, r):
    p = random.randint(l, r)

    arr[p], arr[r] = arr[r], arr[p]
    
    i = l
    for j in range(l, r):
        if arr[j] < arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    arr = [7, 10, 6, 9, 1, 5, 8, 2]
    print(quickmedian(arr))
    print(arr)