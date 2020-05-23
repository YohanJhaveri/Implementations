def bubble_sort(A):
    n = len(A)
    for x in range(n):
        for y in range(n - x - 1):
            if A[y] > A[y+1]:
                A[y], A[y+1] = A[y+1], A[y]

A = [9,2,3,2,6,7,3,2,6]
bubble_sort(A)
print(A)
