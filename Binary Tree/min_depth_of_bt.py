class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minDepth(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return minDepth(root.right) + 1

    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1

# Sample tree builder
def buildTree():
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
    root = buildTree()
    print("Minimum depth of the tree:", minDepth(root))  # Expected: 2
