import random


def quickmedian(arr, l=0, r=None, /, key=lambda x: x):
    if r is None:
        r = len(arr)-1

    return quickselect(arr, (r+l+1)//2+1, l, r, key=key)


def quickselect(arr, k, l=0, r=None, /, key=lambda x: x):
    if r is None:
        r = len(arr)-1

    while l <= r:
        p = partition(arr, l, r, key=key)
        
        if p == k-1:
            return p, arr[p]
        if p > k-1:
            r = p-1
        else:
            l = p+1

    return -1, -1


def partition(arr, l, r, /, key=lambda x: x):
    p = random.randint(l, r)

    arr[p], arr[r] = arr[r], arr[p]
    rk = key(arr[r])
    
    i = l
    for j in range(l, r):
        if key(arr[j]) < rk:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    import time
    
    random.seed(0)
    
    arr = [random.randint(0, 100000) for _ in range(int(1e5))]

    st = time.time()
    for i in range(10):
        quickmedian(arr)
    print(f'QuickSelect: {time.time()-st:0.4g}s')