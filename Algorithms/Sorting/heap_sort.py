import math

def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2

    largest = i

    if l < n and A[largest] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, n, largest)


def heap_sort(A):
    n = len(A)
    for i in range(n//2-1, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

A = [3,5,1,4,8,3,7,8,2,8,4]
heap_sort(A)
print(A)
