class Stack(object):
    class Node(object):
        def __init__(self, v, next=None):
            self.v = v
            self.next = next
        

    def __init__(self, arr):
        self.head = None

        for x in arr:
            self.push(x)
    
    def push(self, x):
        self.head = self.Node(x, self.head)

    def peek(self):
        return self.head.v

    def pop(self):
        node = self.head
        self.head = self.head.next
        return node.v


if __name__ == '__main__':
    stack = Stack([4, 5, 3])
    stack.push(7)

    while stack.head:
        print(stack.pop(), end=' ')
    print()