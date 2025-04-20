class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, x):
    smallerHead = smallerLast = None
    equalHead = equalLast = None
    greaterHead = greaterLast = None
    temp = head
    
    # Traverse the original list and partition it into three lists
    while temp:
        node = Node(temp.data)  # Create a new node with the current data
        
        # Partition into smaller, equal, or greater lists
        if temp.data < x:
            if smallerHead is None:
                smallerHead = node
                smallerLast = smallerHead
            else:
                smallerLast.next = node
                smallerLast = node
        elif temp.data == x:
            if equalHead is None:
                equalHead = node
                equalLast = equalHead
            else:
                equalLast.next = node
                equalLast = node
        else:
            if greaterHead is None:
                greaterHead = node
                greaterLast = greaterHead
            else:
                greaterLast.next = node
                greaterLast = node
        
        temp = temp.next
    
    # Now, combine the three lists together: smaller -> equal -> greater
    if smallerLast:
        smallerLast.next = equalHead
    else:
        smallerHead = equalHead
    
    if equalLast:
        equalLast.next = greaterHead
    else:
        if smallerLast:
            smallerLast.next = greaterHead
        else:
            smallerHead = greaterHead
    
    # Ensure the last node points to None
    if greaterLast:
        greaterLast.next = None
    
    return smallerHead

# Helper functions to create and print a linked list
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def main():
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    x = int(input("Enter the partition value (x): "))
    head = create_linked_list(arr)
    
    print("Original Linked List:")
    print_linked_list(head)

    # Partition the list around the value x
    partitioned_head = partition(head, x)

    print("\nPartitioned Linked List:")
    print_linked_list(partitioned_head)

if __name__ == "__main__":
    main()
