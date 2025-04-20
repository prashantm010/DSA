class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None  # This is the nextRight pointer we want to populate

class Solution:
    def connect(self, root):
        if root is None:
            return None
        
        # Initialize a queue for level order traversal
        q = []
        q.append(root)
        
        # Process nodes level by level
        while len(q) > 0:
            # Number of nodes at the current level
            current_size = len(q)
            
            # Traverse all nodes in the current level
            for i in range(current_size):
                node = q[0]  # Get the front node in the queue
                if i != current_size - 1:
                    node.nextRight = q[1]  # Connect this node's nextRight to the next node in the queue
                
                # Add children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                # Pop the front node
                q.pop(0)

# Main function
def main():
    # Example usage:
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

    sol = Solution()
    sol.connect(root)

    # Printing the nextRight of each node
    print("Node 1 nextRight:", root.nextRight)  # Should be None
    print("Node 2 nextRight:", root.left.nextRight.data)  # Should be 3
    print("Node 3 nextRight:", root.right.nextRight)  # Should be None
    print("Node 4 nextRight:", root.left.left.nextRight.data)  # Should be 5
    print("Node 5 nextRight:", root.left.right.nextRight.data)  # Should be 6
    print("Node 6 nextRight:", root.right.left.nextRight.data)  # Should be 7
    print("Node 7 nextRight:", root.right.right.nextRight)  # Should be None

# Run the main function
if __name__ == "__main__":
    main()
