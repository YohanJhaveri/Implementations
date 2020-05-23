import random, time

def binary_sort(A, bit):
    L, R = [], []

    for num in A:
        if (num >> bit) & 1:  R.append(num)
        else:                 L.append(num)

    if len(set(L)) > 1: L = binary_sort(L, bit-1)
    if len(set(R)) > 1: R = binary_sort(R, bit-1)

    return L + R

def merge(L,R):
    A = []
    while L and R:
        if L[0] < R[0]: A.append(L.pop(0))
        else:           A.append(R.pop(0))
    return A + L + R


def merge_sort(A):
    if len(A) == 1:
        return A
    else:
        mid = len(A) // 2
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L, R)


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

A = [random.randint(0,10000) for x in range(100000)]
B = [random.randint(0,10000) for x in range(100000)]
C = [random.randint(0,10000) for x in range(100000)]
D = [random.randint(0,10000) for x in range(100000)]

start1 = time.time()
A = binary_sort(A, 14)
end1 = time.time()

start2 = time.time()
B = merge_sort(B)
end2 = time.time()

start3 = time.time()
C = quick_sort(C)
end3 = time.time()

start3 = time.time()
C = quick_sort(C)
end3 = time.time()

start4 = time.time()
D.sort()
end4 = time.time()

print('Binary:   ' + str(end1 - start1))
print('Merge:    ' + str(end2 - start2))
print('Quick:    ' + str(end3 - start3))
print('Default:  ' + str(end4 - start4))
# print(A)
