def insertion_sort(A):
    for x in range(len(A)):
        current = x
        while current > 0 and A[current] < A[current - 1]:
            A[current], A[current-1] = A[current-1], A[current]
            current -= 1

A = [9,2,3,2,6,7,3,2,6]
insertion_sort(A)
print(A)
