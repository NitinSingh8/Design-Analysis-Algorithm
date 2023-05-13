class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*i + 1

    def rightChild(self, i):
        return 2*i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def extractMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return min_val


