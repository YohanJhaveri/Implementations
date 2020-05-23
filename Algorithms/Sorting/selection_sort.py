def selection_sort(A):
    for x in range(len(A)):
        m = A[x:].index(min(A[x:]))
        A[x], A[x+m] = A[x+m], A[x]

A = [9,2,3,2,6,7,3,2,6]
selection_sort(A)
print(A)
