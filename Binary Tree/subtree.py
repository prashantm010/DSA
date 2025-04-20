class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def preOrder(self, preOrderList, root):
        if root is None:
            return preOrderList
        preOrderList.append(root.data)
        self.preOrder(preOrderList, root.left)
        self.preOrder(preOrderList, root.right)
        return preOrderList

    def inOrder(self, inOrderList, root):
        if root is None:
            return inOrderList
        self.inOrder(inOrderList, root.left)
        inOrderList.append(root.data)
        self.inOrder(inOrderList, root.right)
        return inOrderList

    def checkIfSubString(self, TinOrder, SinOrder):
        s1 = ','.join(map(str, TinOrder))  # use comma to prevent false matches like 12 vs 1 and 2
        s2 = ','.join(map(str, SinOrder))
        return s1.find(s2) != -1

    def isSubTree(self, T, S):
        TinOrder = self.inOrder([], T)
        TpreOrder = self.preOrder([], T)

        SinOrder = self.inOrder([], S)
        SpreOrder = self.preOrder([], S)

        return (self.checkIfSubString(TinOrder, SinOrder) and
                self.checkIfSubString(TpreOrder, SpreOrder))

# Test case
def buildMainTree():
    root = Node(26)
    root.right = Node(3)
    root.right.right = Node(3)
    root.left = Node(10)
    root.left.left = Node(4)
    root.left.left.right = Node(30)
    root.left.right = Node(6)
    return root

def buildSubTree():
    root = Node(10)
    root.left = Node(4)
    root.left.right = Node(30)
    root.right = Node(6)
    return root

if __name__ == "__main__":
    t = Tree()
    T = buildMainTree()
    S = buildSubTree()
    print("S is subtree of T:", t.isSubTree(T, S))  # Expected: True
