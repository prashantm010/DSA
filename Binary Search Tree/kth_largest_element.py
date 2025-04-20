class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, arr):
        if root is None:
            return arr
        
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
        return arr
    
    def kthLargest(self, root, k):
        if root is None:
            return None
        arr = []
        arr = self.inorder(root, arr)
        n = len(arr)
        if k <= 0 or k > n:
            return None  # k is out of bounds
        return arr[n - k]

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

    # Let's find the 3rd largest element
    k = 3
    result = sol.kthLargest(root, k)

    # Print the result
    if result is not None:
        print(f"The {k}-th largest element is {result}")
    else:
        print(f"The tree does not have {k} elements.")

if __name__ == "__main__":
    main()
