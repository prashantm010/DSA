class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    index = 0
    mp = dict()
    
    def buildTreeUtil(self, ino, pre, start, end):
        if start > end:
            return None
        curr = pre[self.index]
        self.index += 1
        tNode = Node(curr)
        if start == end:
            return tNode
        k = self.mp[curr]
        tNode.left = self.buildTreeUtil(ino, pre, start, k-1)
        tNode.right = self.buildTreeUtil(ino, pre, k+1, end)
        return tNode
    
    def buildtree(self, inorder, preorder, n):
        start = 0
        end = n-1
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i 
        return self.buildTreeUtil(inorder, preorder, start, end)

# Function to print Inorder traversal (to verify the tree)
def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)

# Test the solution
if __name__ == "__main__":
    inorder = [4, 2, 5, 1, 6, 3]
    preorder = [1, 2, 4, 5, 3, 6]
    n = len(inorder)
    
    sol = Solution()
    root = sol.buildtree(inorder, preorder, n)
    
    # Print the inorder traversal of the constructed tree to verify
    print("Inorder traversal of the constructed tree:", inorderTraversal(root))  # Expected Output: [4, 2, 5, 1, 6, 3]
