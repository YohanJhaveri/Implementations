def quick_sort(A):
    pivot = len(A) // 2
    S, E, L = [], [], []

    for index, number in enumerate(A):
        if A[pivot] > A[index]:     S.append(A[index])
        elif A[pivot] < A[index]:   L.append(A[index])
        else:                       E.append(A[index])

    if len(S) > 1: S = quick_sort(S)
    if len(L) > 1: L = quick_sort(L)

    return S + E + L

A = [9,2,3,2,6,7,3,2,6]
A = quick_sort(A)
print(A)
