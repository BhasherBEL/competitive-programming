import generic

class KDTree(generic.KDTree):
    class Node(object):
        def __init__(self, v, dim, l, r, parent):
            self.v:      tuple       = v
            self.dim:    int         = dim
            self.l:      KDTree.Node = l
            self.r:      KDTree.Node = r
            self.parent: KDTree.Node = parent

        # O(log n)
        def nn(self, other):
            if self.l is None and self.l is None:
                return self, self.distance_to_point(other)

            ddist = self.v[self.dim] - other[self.dim]

            child = self.l if self.r is None or self.l is not None and ddist <= 0 else self.r
            ochild = self.r if child is self.l else self.l

            bc, bd = child.nn(other)
            
            if (mdist := self.distance_to_point(other)) < bd:
                bc, bd = self, mdist
            
            if ochild is not None and abs(ddist) < bd:
                oc, od = ochild.nn(other)
                if od < bd:
                    bc, bd = oc, od
            
            return bc, bd

        # TODO
        def knn(self, other, k):
            return

        def distance_to_point(self, other):
            return KDTree.__distanc_btw(self.key, other)

    # O(n log² n)
    def __build(self, vs, curr_dim=0):
        if len(vs) == 0:
            return None
        # vs.sort(key=lambda x: x[curr_dim])
        tree = self.Node(
            v=vs[len(vs)//2],
            dim=curr_dim,
            l=self.__build(vs[len(vs)//2+1:], (curr_dim+1) % self.ndim),
            r=self.__build(vs[:len(vs)//2], (curr_dim+1) % self.ndim),
            parent=None
        )
        if tree.r:
            tree.r.parent = tree
        if tree.l:
            tree.l.parent = tree
        return tree
    
    def __init__(self, coords):
        self.ndim: int         = len(coords[0])
        self.head: KDTree.Node = self.__build(coords)
    
    def nn(self, other):
        return self.head.nn(other)
    
    def knn(self, other, k):
        return self.head.knn(other, k)

    @staticmethod
    def __distanc_btw(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5 


if __name__ == '__main__':
    import numpy as np
    import time
    
    arr = [tuple(x) for x in np.random.randint(0, 1000, (100000, 2))]
    
    st = time.time()
    kdt = KDTree(arr)
    print(f"build time: {time.time()-st:0.4g}s")
