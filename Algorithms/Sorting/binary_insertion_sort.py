def binary_insertion_sort(A):
    tree = []
    
    def insert(tree, x, i, j):
        if i == j:
            tree.insert(i, x)
        else:
            mid = (i + j) // 2
            if x > tree[mid]:
                insert(tree, x, mid+1, j)
            else:
                insert(tree, x, i, mid)

    for x in A:
        insert(tree, x, 0, len(tree))

    return tree

A = [8,5,6,1,4,8,9,2,3,7,7,0]
A = binary_insertion_sort(A)
print(A)
