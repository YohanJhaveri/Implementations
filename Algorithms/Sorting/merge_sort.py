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

print(merge_sort([5,1,6,3,9,7,4,5,2,3,2,4,8]))
