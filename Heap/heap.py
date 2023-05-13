from minheap import MinHeap
from maxheap import MaxHeap


mydata = [2,4,6,8,3,1]

minHeap = MinHeap()

maxHeap = MaxHeap()

for i in mydata:
    minHeap.insert(i)
    maxHeap.insert(i)


for i in range(len(mydata)):
    print(minHeap.extractMin())
    print(maxHeap.extract_max())    


