class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rotateList(head, k):
    if head is None or k == 0:
        return head
    
    # Step 1: Get the length of the list
    length = 1
    t = head
    while t.next:
        length += 1
        t = t.next

    # Step 2: Handle the case where k > length
    k = k % length
    if k == 0:
        return head
    
    # Step 3: Find the new head and tail
    t.next = head  # Make the list circular temporarily
    temp = head
    for _ in range(length - k - 1):
        temp = temp.next
    
    # Step 4: Update the head and break the circular link
    new_head = temp.next
    temp.next = None
    return new_head

# Helper functions to create and print linked lists
def create_linked_list(arr):
    if not arr:
        return None
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
    values = list(map(int, input("Enter list elements (space-separated): ").split()))
    k = int(input("Enter number of rotations: "))
    head = create_linked_list(values)

    print("\nOriginal Linked List:")
    print_linked_list(head)

    rotated_head = rotateList(head, k)

    print("\nRotated Linked List:")
    print_linked_list(rotated_head)

if __name__ == "__main__":
    main()
