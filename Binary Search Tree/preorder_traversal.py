INT_MIN = -454545

class Solution:
    def canRepresentBST(self, arr, N):
        st = []
        root = INT_MIN
        
        for i in arr:
            if i < root:
                return 0  # If current element is smaller than root, it violates the BST property
            
            # Pop elements from the stack until we find the correct root
            while len(st) > 0 and st[-1] < i:
                root = st.pop()
            
            # Push the current element onto the stack
            st.append(i)
        
        return 1  # Return 1 if the array can represent a BST

# Main function to test the code
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()
    
    # Example input
    arr = [40, 30, 35, 80, 100]  # Example preorder traversal array
    N = len(arr)  # Size of the array
    
    # Check if the given array can represent a BST
    result = solution.canRepresentBST(arr, N)
    
    # Output the result
    if result:
        print("The array can represent a Binary Search Tree (BST).")
    else:
        print("The array cannot represent a Binary Search Tree (BST).")
