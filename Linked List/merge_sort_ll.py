class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListOps:
    def getMid(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  

    def sortedMerge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result        

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        mid = self.getMid(head)
        next_to_mid = mid.next
        mid.next = None  # Split into two halves

        left = self.mergeSort(head)
        right = self.mergeSort(next_to_mid)

        sorted_list = self.sortedMerge(left, right)
        return sorted_list

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
    head = create_linked_list(values)

    print("\nOriginal Linked List:")
    print_linked_list(head)

    ops = LinkedListOps()
    sorted_head = ops.mergeSort(head)

    print("\nSorted Linked List:")
    print_linked_list(sorted_head)

if __name__ == "__main__":
    main()
