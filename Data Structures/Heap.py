class MaxHeap():
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        n = len(self.heap) - 1
        self.heapify(n)

    def heapify(self, n):
        parent = n // 2

        if self.heap[parent] < self.heap[n]:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            self.heapify(parent)

    def __str__(self):
        return str(self.heap)


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(3)
max_heap.insert(5)
max_heap.insert(2)
max_heap.insert(4)
max_heap.insert(1)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(9)
print(max_heap)
