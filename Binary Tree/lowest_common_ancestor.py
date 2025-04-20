class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def lca(self, root, n1, n2):
        # Base case: If root is None, return None
        if root is None:
            return None
        
        # If root matches n1 or n2, return root
        if root.data == n1 or root.data == n2:
            return root
        
        # Recursively find LCA in left and right subtrees
        left_lca = self.lca(root.left, n1, n2)
        right_lca = self.lca(root.right, n1, n2)
        
        # If both left and right subtrees have nodes matching n1 or n2, the current node is the LCA
        if left_lca and right_lca:
            return root
        
        # Otherwise, return the non-null node if either left or right has a match
        return left_lca if left_lca else right_lca

# Main function
def main():
    # Example usage:
    #      1
    #    /   \
    #   2     3
    #  / \   / \
    # 4   5 6   7
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    
    # Test cases for LCA
    lca_node = sol.lca(root, 4, 5)  # LCA of 4 and 5
    print(f"LCA of 4 and 5: {lca_node.data if lca_node else 'None'}")
    
    lca_node = sol.lca(root, 4, 6)  # LCA of 4 and 6
    print(f"LCA of 4 and 6: {lca_node.data if lca_node else 'None'}")
    
    lca_node = sol.lca(root, 3, 4)  # LCA of 3 and 4
    print(f"LCA of 3 and 4: {lca_node.data if lca_node else 'None'}")
    
    lca_node = sol.lca(root, 2, 7)  # LCA of 2 and 7
    print(f"LCA of 2 and 7: {lca_node.data if lca_node else 'None'}")

# Run the main function
if __name__ == "__main__":
    main()
