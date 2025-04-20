class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def printLeaf(self, arr, root):
        if root is None:
            return
        self.printLeaf(arr, root.left)
        if root.left is None and root.right is None:
            arr.append(root.data)
        self.printLeaf(arr, root.right)
        
    def printLeftBoundary(self, arr, root):
        if root:
            if root.left:
                arr.append(root.data)
                self.printLeftBoundary(arr, root.left)
            elif root.right:
                arr.append(root.data)
                self.printLeftBoundary(arr, root.right)
                
    def printRightBoundary(self, arr, root):
        if root:
            if root.right:
                self.printRightBoundary(arr, root.right)
                arr.append(root.data)
            elif root.left:
                self.printRightBoundary(arr, root.left)
                arr.append(root.data)
                
    def printBoundaryView(self, root):
        if root is None:
            return []
        arr = []
        arr.append(root.data)
        self.printLeftBoundary(arr, root.left)
        self.printLeaf(arr, root.left)
        self.printLeaf(arr, root.right)  
        self.printRightBoundary(arr, root.right)
        return arr


# Main function to test the solution
def main():
    # Create the tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5  6  7
    #             \
    #              8

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)

    sol = Solution()
    boundary = sol.printBoundaryView(root)
    
    print("Boundary View of the tree:")
    print(boundary)

# Run the main function
if __name__ == "__main__":
    main()
