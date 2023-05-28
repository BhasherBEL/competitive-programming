def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    l = mergeSort(arr[:len(arr)//2])
    r = mergeSort(arr[len(arr)//2:])

    res = []

    while l or r:
        if l and (not r or l[0] < r[0]):
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))

    return res


if __name__ == '__main__':
    print(mergeSort([4, 2, 3, 6, 5, 1, 2]))
