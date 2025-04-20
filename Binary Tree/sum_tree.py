class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isleaf(self, root):
        """Check if a node is a leaf."""
        return root is not None and root.left is None and root.right is None
    
    def isSumTree(self, root):
        """Check if the binary tree is a Sum Tree."""
        # Base case: An empty tree or a leaf node is a Sum Tree
        if root is None or self.isleaf(root):
            return True
        
        # Recursively check left and right subtrees
        if self.isSumTree(root.left) and self.isSumTree(root.right):
            # Get the sum of left and right subtrees
            left_sum = 0 if root.left is None else root.left.data
            right_sum = 0 if root.right is None else root.right.data

            # The node's data must be the sum of the left and right subtree data
            if root.data == left_sum + right_sum:
                return True
        return False

# Main function to test the solution
def main():
    # Creating a Sum Tree:
    #        26
    #       /  \
    #      10   3
    #     /  \   \
    #    4   6    3
    
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    
    sol = Solution()
    if sol.isSumTree(root):
        print("The tree is a Sum Tree.")
    else:
        print("The tree is not a Sum Tree.")

# Run the main function
if __name__ == "__main__":
    main()
