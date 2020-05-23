def digit_sort(A, n):
    digits = {x:[] for x in range(10)}
    for x in A:
        digits[(x // 10**n) % 10].append(x)

    A = []

    for x in digits:
        A.extend(digits[x])

    return A

def radix_sort(A):
    for i in range(len(str(A[0]))):
        A = digit_sort(A, i)
    return A

A = [34,56,42,56,27,68,14,24,36,21,27]
A = radix_sort(A)
print(A)
