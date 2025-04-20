class Solution:
    # Inorder traversal to store the elements in a sorted array
    def inorder(self, root, arr):
        if root is None:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
    
    # Function to check if there is a pair with sum equal to the target
    def isPairPresent(self, root, target): 
        arr = []
        self.inorder(root, arr)  # Get the inorder traversal of the BST
        
        start = 0
        end = len(arr) - 1
        
        # Two-pointer approach
        while start < end:
            current_sum = arr[start] + arr[end]
            if current_sum == target:
                return 1  # Pair found
            elif current_sum < target:
                start += 1  # Move start pointer to the right to increase sum
            else:
                end -= 1  # Move end pointer to the left to decrease sum
        
        return 0  # No pair found

# Helper function to create a binary search tree (BST)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example of usage
def main():
    # Create a sample BST
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(18)
    root.right.right = Node(25)
    
    # Set the target sum
    target = 28
    
    # Create solution object and call isPairPresent function
    sol = Solution()
    result = sol.isPairPresent(root, target)
    
    # Print result
    if result:
        print("Pair found")
    else:
        print("Pair not found")

if __name__ == "__main__":
    main()
