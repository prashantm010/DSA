class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head, k):
    if head is None:
        return None
    
    # Reverse the first k nodes
    prev = None
    current = head
    count = 0
    
    # Reverse k nodes
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    
    # Now current points to the (k+1)th node, recursively reverse the rest of the list
    if current:
        head.next = reverse(current, k)
    
    # prev is the new head of the reversed list
    return prev

# Helper function to create a linked list
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def main():
    # Creating a linked list for testing: 1 -> 2 -> 3 -> 4 -> 5 -> None
    arr = list(map(int, input("Enter list elements (space-separated): ").split()))
    k = int(input("Enter the size of group (k): "))
    head = create_linked_list(arr)
    
    print("Original Linked List:")
    print_linked_list(head)

    # Reverse in groups of k
    head = reverse(head, k)

    print("\nReversed Linked List in groups of k:")
    print_linked_list(head)

if __name__ == "__main__":
    main()
