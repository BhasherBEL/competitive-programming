from math import log, inf

from algorithms.selection.quickSelect.inplace import quickmedian
import generic

class KDTree(generic.KDTree):
    # O(n log n)
    def __setup(self, l, r, i=1, dim=0):
        if l >= r:
            if l == r:
                self.tree[i] = self.coords[l]
            return
        p, self.tree[i] = quickmedian(self.coords, l, r, key=lambda x: x[dim])

        self.__setup(l, p-1, 2*i, (dim+1)%self.ndim)
        self.__setup(p+1, r, 2*i+1, (dim+1)%self.ndim)

    def __init__(self, coords):
        self.coords = coords
        depth = int(log(len(coords), 2))+1
        self.size = 2**depth
        self.tree = [None] * self.size
        self.ndim = len(coords[0])

        self.__setup(0, len(coords)-1)

    @staticmethod
    def __distance(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5 
    
    # O(log n)
    def nn(self, other, i=1, exclude_self=False, limit=inf):
        dist = self.__distance(self.tree[i], other)
        if self.size < 2*i+1 or self.tree[2*i] is None and self.tree[2*i+1] is None:
            if exclude_self and other == self.tree[i]:
                return None, inf
            else:
                return self.tree[i], dist
        
        dim = int(log(i, 2))%self.ndim
        ddist = self.tree[i][dim] - other[dim]

        cond = self.tree[2*i] is None or self.tree[2*i+1] is not None and ddist <= 0
        child = 2*i + cond
        ochild = 2*i + 1-cond

        bc, bd = self.nn(other, child, exclude_self=exclude_self, limit=limit)

        if dist < bd and (not exclude_self or other != self.tree[i]):
            bc, bd = self.tree[i], dist
 
        if abs(ddist) < limit and self.tree[ochild] is not None and abs(ddist) < bd:
            oc, od = self.nn(other, ochild, exclude_self=exclude_self, limit=limit)
            if od < bd:
                bc, bd = oc, od

        return bc, bd

    # TODO
    def knn(self, other, k):
        return



if __name__ == '__main__':
    import numpy as np
    import time
    
    arr = [tuple(x) for x in np.random.randint(0, 1000, (100000, 2))]
    
    st = time.time()
    kdt = KDTree(arr)
    print(f"build time: {time.time()-st:0.4g}s")
