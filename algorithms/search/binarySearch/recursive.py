def binarySearch(data, key, l=0, r=None):
    if r is None:
        r = len(data)-1
    
    if l == r:
        return l

    m = (l+r)//2

    if data[m] < key:
        return binarySearch(data, key, m+1, r)
    if data[m] > key:
        return binarySearch(data, key, l, m)
    return m


if __name__ == '__main__':
    data = [1, 1, 4, 7, 7, 8]

    print(binarySearch(data, 2))
