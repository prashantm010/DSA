class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.data <= b.data:
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)
    
    result.next = None  # Right pointer should be None
    return result

def flatten(root):
    if not root or not root.next:
        return root
    
    # Recursively flatten the right side of the list
    root.next = flatten(root.next)
    
    # Merge current list with the next flattened list
    root = merge(root, root.next)
    
    return root

# Helper functions to create and print the linked list
def print_linked_list(root):
    while root:
        print(root.data, end=" -> ")
        root = root.bottom
    print("None")

def create_list(arr):
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def main():
    # Creating a 2D linked list (linked lists within linked lists)
    # Example:    5 -> 10 -> 19 -> 28
    #              |     |     |     |
    #              7     20    22    35
    #              |           |
    #              8          50

    root = Node(5)
    root.bottom = Node(7)
    root.bottom.bottom = Node(8)

    root.next = Node(10)
    root.next.bottom = Node(20)

    root.next.next = Node(19)
    root.next.next.bottom = Node(22)

    root.next.next.next = Node(28)
    root.next.next.next.bottom = Node(35)
    root.next.next.next.bottom.bottom = Node(50)

    print("Original 2D Linked List:")
    print_linked_list(root)

    flattened = flatten(root)

    print("\nFlattened Linked List:")
    print_linked_list(flattened)

if __name__ == "__main__":
    main()
