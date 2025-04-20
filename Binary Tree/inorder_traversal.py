class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    res = []
    st = []
    current = root
    while True:
        if current is not None:
            st.append(current)
            current = current.left
        elif st:
            temp = st.pop()
            res.append(temp.data)
            current = temp.right
        else:
            break
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
    print("Inorder traversal:", inOrder(root))  # Expected Output: [4, 2
