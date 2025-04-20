import collections

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        # Queue to perform BFS (stores node and its horizontal distance)
        queue = collections.deque([(root, 0)])
        
        # Maps horizontal distance to nodes at that distance
        mp = collections.defaultdict(list)
        
        # Track the minimum and maximum horizontal distance
        min_hd = max_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            mp[hd].append(node.data)
            
            # Update the min and max horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # Add the left child with hd - 1
            if node.left:
                queue.append((node.left, hd - 1))
            
            # Add the right child with hd + 1
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Prepare the result by traversing the map in sorted order of horizontal distances
        res = []
        for hd in range(min_hd, max_hd + 1):
            res.extend(mp[hd])  # Append all nodes at the current horizontal distance
        
        return res

# Sample binary tree:
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

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = buildTree()
    sol = Solution()
    print("Vertical order traversal:", sol.verticalOrder(root))
