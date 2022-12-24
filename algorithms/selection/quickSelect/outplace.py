import random


def quickmedian(arr, key=lambda x: x):
    return quickselect(arr, k=len(arr)//2, key=key)


def quickselect(arr, k, key=lambda x: x):
    lo, pi, hi = partition(arr, key=key)
    p = len(lo)+1

    if p == k:
        return pi
    if p > k:
        return quickselect(lo, k)
    return quickselect(hi, k-p)


def partition(arr, key=lambda x: x):
    p = random.randint(0, len(arr)-1)
    pv = key(arr[p])
    lo, hi = [], []
    
    for i in range(0, len(arr)):
        if i != p:
            if key(arr[i]) <= pv:
                lo.append(arr[i])
            else:
                hi.append(arr[i])

    return lo, arr[p], hi


if __name__ == '__main__':
    import time
    
    random.seed(0)

    arr = [random.randint(0, 100000) for _ in range(int(1e5))]

    st = time.time()
    for i in range(10):
        quickmedian(arr)
    print(f'QuickSelect: {time.time()-st:0.4g}s')