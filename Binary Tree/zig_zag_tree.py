class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigzagTree(root):
    if not root:
        return []
    
    currentLevel = [root]
    nextLevel = []
    result = []
    leftToRight = True

    while currentLevel:
        node = currentLevel.pop()
        result.append(node.data)

        # Direction-dependent children push
        if leftToRight:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        else:
            if node.right:
                nextLevel.append(node.right)
            if node.left:
                nextLevel.append(node.left)

        # If current level is done, swap and change direction
        if not currentLevel:
            currentLevel, nextLevel = nextLevel, []
            leftToRight = not leftToRight

    return result

def buildTree():
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def main():
    root = buildTree()
    print("Zigzag Traversal of the Tree:")
    print(zigzagTree(root))  # Expected: [1, 3, 2, 4, 5, 6, 7]

if __name__ == "__main__":
    main()
