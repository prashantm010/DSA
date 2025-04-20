class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return True
    return isSymmetricUtil(root.left, root.right)

def isSymmetricUtil(root1, root2):
    if root1 is None and root2 is None:
        return True
        
    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return isSymmetricUtil(root1.left, root2.right) and isSymmetricUtil(root1.right, root2.left)
    
    return False

# Helper function to build a sample symmetric tree
def buildSampleTree():
    #         1
    #       /   \
    #      2     2
    #     / \   / \
    #    3   4 4   3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    return root

# Helper function to build a non-symmetric tree
def buildNonSymmetricTree():
    #         1
    #       /   \
    #      2     2
    #       \     \
    #        3     3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.right = Node(3)
    root.right.right = Node(3)
    return root

def main():
    print("Checking symmetric tree:")
    root1 = buildSampleTree()
    print("Is symmetric?", isSymmetric(root1))  # Expected: True

    print("\nChecking non-symmetric tree:")
    root2 = buildNonSymmetricTree()
    print("Is symmetric?", isSymmetric(root2))  # Expected: False

if __name__ == "__main__":
    main()
