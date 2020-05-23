def count_sort(A):
    counts = [0 for x in range(max(A) - min(A) + 1)]
    for x in A:
        counts[x-min(A)] += 1

    x = 0
    for index, count in enumerate(counts):
        A[x:x+count] = [index + min(A)] * count
        x += count

    return A

A = [3,6,2,5,7,8,4,4,6,7,2]
A = count_sort(A)
print(A)
