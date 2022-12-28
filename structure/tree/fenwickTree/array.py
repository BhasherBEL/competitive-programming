class FenwichTree(object):
    def __init__(self, arr):
        self.size = len(arr)
        self.arr = arr
        for i in range(1, self.size):
            j = i + i&(-i)
            if j < self.size:
                arr[j] += arr[i]

    def get(self, i):
        res = self.arr[0]
        while i > 0:
            res += self.arr[i]
            i -= i&(-i)
        return res

    def update(self, i, dv):
        while i < self.size:
            self.arr[i] += dv
            i += i&(-i)


if __name__ == '__main__':
    ft = FenwichTree([1, 2, 3, 4, 5])

    print(ft.get(3))
    ft.update(2, 5)
    print(ft.get(3))
