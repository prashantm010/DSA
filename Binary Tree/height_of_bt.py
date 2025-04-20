class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

def buildSampleTree():
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    return root

if __name__ == "__main__":
    tree = BinaryTree()
    root = buildSampleTree()
    print("Height of the tree:", tree.height(root))  # Expected output: 3
