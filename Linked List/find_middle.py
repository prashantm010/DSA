class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMid(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

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
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def main():
    values = list(map(int, input("Enter list elements (space-separated): ").split()))
    head = create_linked_list(values)

    print("Linked List:")
    print_linked_list(head)

    if head:
        middle = findMid(head)
        print("Middle element:", middle)
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
