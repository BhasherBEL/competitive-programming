import generic

class SegmentTree(generic.SegmentTree):
    class Node:
        def __init__(self, k, v, l, r, parent=None):
            self.k:      tuple            = k
            self.v:      any              = v
            self.l:      SegmentTree.Node = l
            self.r:      SegmentTree.Node = r
            self.parent: SegmentTree.Node = parent
        
        def get(self, i, j, fn):
            if i == self.k[0] and j == self.k[1]:
                return self.v
            if j <= self.l.k[1]:
                return self.l.get(i, j, fn)
            if i >= self.r.k[0]:
                return self.r.get(i, j, fn)
            return fn(self.l.get(i, self.l.k[1], fn), self.r.get(self.r.k[0], j, fn))

        def update(self, p, v, fn):
            if p == self.k[0] == self.k[1]:
                self.v = v
                return
            if p <= self.l.k[1]:
                self.l.update(p, v, fn)
            else:
                self.r.update(p, v, fn)

            self.v = fn(self.l.v, self.r.v)

    def __build(self, i, j):
        if i == j:
            return SegmentTree.Node((i, j), self.arr[i], None, None)

        p = (i+j)//2
        tree = SegmentTree.Node(
            (i, j),
            self.default,
            self.__build(i, p),
            self.__build(p+1, j)
        )
        tree.v = self.fn(tree.l.v, tree.r.v)
        return tree
        
    def __init__(self, arr, fn, default=0):
        self.arr:     list             = arr
        self.size:    int              = len(arr)
        self.fn:      function         = fn
        self.default: any              = default
        self.head:    SegmentTree.Node = self.__build(0, self.size-1)

    def get(self, i, j):
        return self.head.get(i, j, self.fn)

    def update(self, p, v):
        return self.head.update(p, v, self.fn)


if __name__ == "__main__":
    st = SegmentTree(
        [1, 4, 8, 2, 1, 9, 4],
        lambda a, b: a+b,
        default=1
    )

    st.update(1, 5)

    print(st.get(1, 4))