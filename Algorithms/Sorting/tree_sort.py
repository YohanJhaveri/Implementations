class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right == None:
                        current.right = Node(data)
                        return
                    else:
                        current = current.right
                else:
                    if current.left == None:
                        current.left = Node(data)
                        return
                    else:
                        current = current.left

    def inorder(self):
        tree = []
        def traverse(node):
            if node.left != None: traverse(node.left)
            tree.append(node.data)
            if node.right != None: traverse(node.right)
        traverse(self.root)
        return tree

def tree_sort(A):
    bt = BinaryTree()
    for x in A:
        bt.add(x)
    return bt.inorder()


A = [8,5,6,1,4,9,2,3,7,0]
A = tree_sort(A)
print(A)
