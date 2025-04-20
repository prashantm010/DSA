class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.h = 0

def diameterUtil(root, height):
    if root is None:
        height.h = 0
        return 0

    lh = Height()
    rh = Height()

    # Get the diameter of left and right subtrees
    ld = diameterUtil(root.left, lh)
    rd = diameterUtil(root.right, rh)

    # Height of current node
    height.h = max(lh.h, rh.h) + 1

    # Diameter is max of:
    # 1. Left diameter
    # 2. Right diameter
    # 3. Height of left + right + 1 (through current node)
    return max(ld, rd, lh.h + rh.h + 1)

def diameter(root):
    height = Height()
    return diameterUtil(root, height)

def buildSampleTree():
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

if __name__ == "__main__":
    root = buildSampleTree()
    print("Diameter of the tree is:", diameter(root))  # Expected: 4
