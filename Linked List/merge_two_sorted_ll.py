class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortedMerge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        result = head1
        result.next = sortedMerge(head1.next, head2)
    else:
        result = head2
        result.next = sortedMerge(head1, head2.next)

    return result

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
    list1 = list(map(int, input("Enter sorted list 1 (space-separated): ").split()))
    list2 = list(map(int, input("Enter sorted list 2 (space-separated): ").split()))

    head1 = create_linked_list(list1)
    head2 = create_linked_list(list2)

    merged_head = sortedMerge(head1, head2)

    # Output
    print("Merged Sorted Linked List:")
    print_linked_list(merged_head)

if __name__ == "__main__":
    main()
