class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def merge(self, root1, root2):
        res = []
        s1, s2, curr1, curr2 = [], [], root1, root2
        
        # Traverse the leftmost nodes of both trees
        while curr1:
            s1.append(curr1)
            curr1 = curr1.left
        while curr2:
            s2.append(curr2)
            curr2 = curr2.left
        
        # Merge the two trees
        while s1 or s2:
            item1 = item2 = None
            if s1:
                item1 = s1[-1]
            if s2:
                item2 = s2[-1]
                
            if item1 and item2:
                if item1.data <= item2.data:
                    res.append(item1.data)
                    s1.pop()
                    # Traverse the right subtree of the popped item1 node
                    curr1 = item1.right
                    while curr1:
                        s1.append(curr1)
                        curr1 = curr1.left
                else:
                    res.append(item2.data)
                    s2.pop()
                    # Traverse the right subtree of the popped item2 node
                    curr2 = item2.right
                    while curr2:
                        s2.append(curr2)
                        curr2 = curr2.left
            elif item1:
                res.append(item1.data)
                s1.pop()
                curr1 = item1.right
                while curr1:
                    s1.append(curr1)
                    curr1 = curr1.left
            elif item2:
                res.append(item2.data)
                s2.pop()
                curr2 = item2.right
                while curr2:
                    s2.append(curr2)
                    curr2 = curr2.left
        
        return res

# Example to test the solution
if __name__ == "__main__":
    # Tree 1
    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)
    root1.left.right = Node(2)
    
    # Tree 2
    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(6)
    
    solution = Solution()
    result = solution.merge(root1, root2)
    print(result)  # This will print the merged sorted list
