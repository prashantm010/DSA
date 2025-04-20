class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def isBSTUtil(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = Node(nums[mid])
        root.left = self.isBSTUtil(nums, start, mid - 1)
        root.right = self.isBSTUtil(nums, mid + 1, end)
        return root
        
    def preOrderTraversal(self, root, arr):
        if root is None:
            return arr
        arr.append(root.data)
        self.preOrderTraversal(root.left, arr)
        self.preOrderTraversal(root.right, arr)
        return arr
    
    def sortedArrayToBST(self, nums):
        end = len(nums) - 1
        start = 0
        root = self.isBSTUtil(nums, start, end)
        res = []
        res = self.preOrderTraversal(root, res)
        return res


# Main function to test the solution
def main():
    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    res = sol.sortedArrayToBST(nums)
    print("Pre-order traversal of the BST:", res)

# Run the main function
if __name__ == "__main__":
    main()
