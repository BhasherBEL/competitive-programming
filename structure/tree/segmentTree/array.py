import generic

class SegmentTree(generic.SegmentTree):
    def __init__(self, arr, fn, default=0):
        self.size = len(arr)
        self.tree = [default] * self.size + arr
        self.fn = fn
        self.default = default
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = fn(self.tree[2*i], self.tree[2*i+1])

    def get(self, i, j):
        i += self.size
        j += self.size
        res = self.default
        while i < j:
            if i&1:  # i%2 == 1
                res = self.fn(res, self.tree[i])
                i += 1 
            if j&1:  # j%2 == 1
                j -= 1
                res = self.fn(res, self.tree[j])
            i //= 2
            j //= 2
        return res

    def update(self, p, v):
        p += self.size
        self.tree[p] = v
        while p > 1:
            p //= 2
            self.tree[p] = self.fn(self.tree[p*2], self.tree[p*2+1])


if __name__ == "__main__":
    st = SegmentTree(
        [1, 4, 8, 2, 1, 9, 4],
        lambda a, b: a*b,
        default=1
    )

    print(st.get(1, 4))