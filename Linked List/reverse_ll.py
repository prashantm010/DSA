class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    c = head
    while c:
        next_node = c.next
        c.next = prev
        prev = c
        c = next_node
    return prev

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        current.next = Node(data)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def main():
    values = list(map(int, input("Enter list elements (space-separated): ").split()))
    head = create_linked_list(values)
    print_linked_list(head)
    reversed_head = reverse(head)
    print("Reversed Linked List:")
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
