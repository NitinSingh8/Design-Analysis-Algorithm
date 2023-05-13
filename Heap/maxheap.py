class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index-1)//2
    
    def left(self, index):
        return 2*index+1
    def right(self, index):
        return 2*index+2
    
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap)-1
        while index != 0 and self.heap[self.parent(index)]<self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
        
    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        largest = index
        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest = left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest = right
        if largest!=index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)
        
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] =self.heap.pop()
        self.heapify(0)
        return max_value

