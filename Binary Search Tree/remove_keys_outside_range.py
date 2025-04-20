class Solution:
    def removekeys(self, root, l, r):
        if root is None:
            return None
        
        # Recur for left and right subtrees
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)
        
        # If current node's data is less than l, we return the right child
        if root.data < l:
            return root.right
        
        # If current node's data is greater than r, we return the left child
        if root.data > r:
            return root.left
        
        # If current node is within the range, we return the node itself
        return root

# Helper function to print the inorder traversal of the tree
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)

# Main function to test
def main():
    # Create a BST
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.right.right = Node(35)

    # Set the range [l, r]
    l, r = 10, 30

    # Create a solution object and call removekeys
    sol = Solution()
    root = sol.removekeys(root, l, r)

    # Print the inorder traversal of the modified tree
    print("Inorder traversal after removing keys outside the range [l, r]:")
    print(inorder(root))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

if __name__ == "__main__":
    main()
