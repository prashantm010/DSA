def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def checkForBalancedTree(root):
    if root is None:
        return True  # An empty tree is balanced

    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <= 1 and
        checkForBalancedTree(root.left) and
        checkForBalancedTree(root.right)):
        return True

    return False

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildBalancedTree():
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

def buildUnbalancedTree():
    #       1
    #      /
    #     2
    #    /
    #   3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    return root

def main():
    print("Balanced Tree:")
    balanced_root = buildBalancedTree()
    print("Is Balanced?", checkForBalancedTree(balanced_root))  # Expected: True

    print("\nUnbalanced Tree:")
    unbalanced_root = buildUnbalancedTree()
    print("Is Balanced?", checkForBalancedTree(unbalanced_root))  # Expected: False

if __name__ == "__main__":
    main()
