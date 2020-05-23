class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        node = self.root
        while True:
            if node == None:
                self.root = Node(x)
                break

            if x > node.data:
                if node.right != None:
                    node = node.right
                else:
                    node.right = Node(x)
                    break
            else:
                if node.left != None:
                    node = node.left
                else:
                    node.left = Node(x)
                    break

    def inorder(self):
        def traverse(node):
            if node.left != None: traverse(node.left)
            print(node.data)
            if node.right != None: traverse(node.right)
        traverse(self.root)


bt = BinaryTree()
bt.insert(8)
bt.insert(3)
bt.insert(5)
bt.insert(2)
bt.insert(4)
bt.insert(1)
bt.insert(7)
bt.insert(6)
bt.inorder()
