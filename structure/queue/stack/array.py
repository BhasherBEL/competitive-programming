class Stack(object):
    def __init__(self, arr):
        self.arr = arr[::-1]
        self.arr.append(5)
    
    def push(self, x):
        self.arr.append(x)

    def peek(self):
        return self.arr[len(self.arr)-1]

    def pop(self):
        return self.arr.pop()


if __name__ == '__main__':
    stack = Stack([4, 5, 3])
    stack.push(7)
