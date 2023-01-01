class BinarySearchTree(object):
    class Node(object):
        def __init__(self, k, v, l=None, r=None):
            self.k = k
            self.v = v
            self.l = l
            self.r = r

        def __repr__(self) -> str:
            return f'BST<k={self.k},v={self.v}{",l=" + str(self.l) if self.l else ""}{",r=" + str(self.r) if self.r else ""}>'
        
    
    def __init__(self):
        self.head = None
    
    def insert(self, k, v):
        if not self.head:
            self.head = self.Node(k, v)
            return

        parent = self.head
        while (child := parent.l if parent.k >= k else parent.r) is not None:
            parent = child

        if parent.k >= k:
            parent.l = self.Node(k, v)
        else:
            parent.r = self.Node(k, v)

    def __repr__(self):
        return str(self.head)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(4, 0)
    bst.insert(3, 0)
    bst.insert(7, 0)
    bst.insert(2, 0)
    print(bst)
        