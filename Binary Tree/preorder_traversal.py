class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    res = []
    current = root
    st = [current]
    while len(st) > 0:
        current = st.pop()
        res.append(current.data)
        if current.right is not None:
            st.append(current.right)        
        if current.left is not None:
            st.append(current.left)
    return res

# Sample tree:
#         1
#        / \
#       2   3
#      / \    
#     4   5   

def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

if __name__ == "__main__":
    root = buildTree()
    print("Preorder traversal:", preOrder(root))  # Expected Output: [1, 2, 4, 5, 3]
