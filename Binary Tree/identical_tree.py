class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def isIdentical(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.data != root2.data:
                return False
            return (self.isIdentical(root1.left, root2.left) and
                    self.isIdentical(root1.right, root2.right))

        return False

def buildTree1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

def buildTree2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

if __name__ == "__main__":
    bt = BinaryTree()
    tree1 = buildTree1()
    tree2 = buildTree2()
    print("Trees are identical:", bt.isIdentical(tree1, tree2))  # Expected: True
