def binarySearch(data, key):
    l = 0
    r = len(data)-1

    while l != r:
        m = (l+r)//2
        if data[m] < key:
            l = m+1
        elif data[m] > key:
            r = m
        else:
            return m
    
    return l


if __name__ == '__main__':
    data = [1, 1, 4, 7, 7, 8]

    print(binarySearch(data, 2))
