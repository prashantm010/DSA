class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, x):
        # Initialize successor as None
        suc = None
        
        # Traverse the tree
        while root:
            if x.data < root.data:
                suc = root  # Potential successor
                root = root.left  # Move to the left subtree
            else:
                root = root.right  # Move to the right subtree
        
        return suc

def main():
    # Create the BST
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.right.right = Node(35)

    # Create a solution object
    sol = Solution()

    # Let's assume we are finding the inorder successor of node with data 15
    x = root.left.right  # Node with value 15
    successor = sol.inorderSuccessor(root, x)

    # Print the successor
    if successor:
        print(f"The inorder successor of {x.data} is {successor.data}")
    else:
        print(f"The node {x.data} has no inorder successor.")

if __name__ == "__main__":
    main()
