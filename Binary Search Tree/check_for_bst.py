INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isBSTUtil(self, root, min, max):
        if root is None:
            return True
        
        if root.data <= min or root.data >= max:
            return False
        
        return self.isBSTUtil(root.left, min, root.data) and self.isBSTUtil(root.right, root.data, max)
    
    def isBST(self, root):
        return self.isBSTUtil(root, INT_MIN, INT_MAX)

# Main function to test the solution
def main():
    # Creating a Binary Search Tree:
    #        10
    #       /  \
    #      5    20
    #     / \   / \
    #    3   8 15  30
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.left = Node(15)
    root.right.right = Node(30)
    
    sol = Solution()
    if sol.isBST(root):
        print("The tree is a Binary Search Tree.")
    else:
        print("The tree is not a Binary Search Tree.")

# Run the main function
if __name__ == "__main__":
    main()
