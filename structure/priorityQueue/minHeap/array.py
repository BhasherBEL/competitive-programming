class MinHeap(object):
    def __init__(self, arr):
        self.size = len(arr)
        self.arr: list = arr
        # TODO

    def push(self, x):
        self.arr.append(x)
        self.size += 1
        self.heapifyUp(self.size-1)

    def peek(self):
        return self.arr[0]

    def pop(self):
        item = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.size -= 1
        self.heapifyDown(0)
        return item
    
    def pushpop(self, x):
        item = self.arr[0]
        self.arr[0] = x
        self.heapifyDown(0)
        return item
    
    def heapifyUp(self, i):
        while i > 0 and self.arr[(p := (i-1)//2)] > self.arr[i]:
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def heapifyDown(self, i):
        while (l := i*2+1) < self.size:
            j = l if (r := i*2+2) >= self.size or self.arr[l] <= self.arr[r] else r
            if self.arr[i] <= self.arr[j]:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j

if __name__ == '__main__':
    pq = MinHeap([])
    pq.push(2) 
    pq.push(1) 
    pq.push(3) 
    pq.push(0) 
    pq.push(4)
    pq.pushpop(7)
    print(pq.pop())
    print(pq.arr)