class Dequeue(object):
    class Node(object):
        def __init__(self, v, previous=None, next=None):
            self.v = v
            self.previous = previous
            self.next = next
        

    def __init__(self, arr):
        self.head = None
        self.rear = None

        for x in arr:
            self.pushright(x)
    
    def pushright(self, x):
        node = self.Node(x, previous=self.rear)
        if self.rear:
            self.rear.next = node
        else:
            self.head = node
        self.rear = node

    def pushleft(self, x):
        node = self.Node(x, next=self.head)
        if self.head:
            self.head.previous = node
        else:
            self.rear = node
        self.head = node

    def peekleft(self):
        return self.head.v

    def peekright(self):
        return self.rear.v

    def popleft(self):
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.read = None
        return node.v

    def popright(self):
        node = self.rear
        self.rear = self.rear.previous
        if self.rear:
            self.rear.next = None
        else:
            self.head = None
        return node.v



if __name__ == '__main__':
    queue = Dequeue([4, 5, 3])
    queue.pushleft(7)

    while queue.head:
        print(queue.popright(), end=' ')
    print()