class Queue(object):
    class Node(object):
        def __init__(self, v, next=None):
            self.v = v
            self.next = next
        

    def __init__(self, arr):
        self.head = None
        self.rear = None

        for x in arr:
            self.push(x)
    
    def push(self, x):
        node = self.Node(x)
        if self.rear:
            self.rear.next = node
        else:
            self.head = node
        self.rear = node

    def peek(self):
        return self.head.v

    def pop(self):
        node = self.head
        self.head = self.head.next
        if not self.head:
            self.read = None
        return node.v


if __name__ == '__main__':
    queue = Queue([4, 5, 3])
    queue.push(7)

    while queue.head:
        print(queue.pop(), end=' ')
    print()