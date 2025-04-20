class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(node):
    if node is None or node.next is None:
        print("Can't delete the last node with this method!")
        return
    node.data = node.next.data
    node.next = node.next.next

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def find_node(head, value):
    current = head
    while current:
        if current.data == value:
            return current
        current = current.next
    return None

def main():
    values = list(map(int, input("Enter list elements (space-separated): ").split()))
    to_delete = int(input("Enter value to delete (not the last element): "))
    head = create_linked_list(values)
    print_linked_list(head)

    node_to_delete = find_node(head, to_delete)
    if node_to_delete is None:
        print("Value not found in list.")
    elif node_to_delete.next is None:
        print("Cannot delete the last node using this method.")
    else:
        delete(node_to_delete)
        print("Linked List after deletion:")
        print_linked_list(head)

if __name__ == "__main__":
    main()
