class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListOps:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addTwoLists(self, first, second):
        carry = 0
        head = None
        prev = None
        temp = None

        first = self.reverse(first)
        second = self.reverse(second)

        while first or second:
            fdata = first.data if first else 0
            sdata = second.data if second else 0
            total = fdata + sdata + carry
            carry = total // 10
            digit = total % 10
            temp = Node(digit)

            if head is None:
                head = temp
            else:
                prev.next = temp
            prev = temp

            if first:
                first = first.next
            if second:
                second = second.next

        if carry > 0:
            prev.next = Node(carry)

        return self.reverse(head)

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

def main():
    values1 = list(map(int, input("Enter digits of first number (space-separated): ").split()))
    values2 = list(map(int, input("Enter digits of second number (space-separated): ").split()))

    first = create_linked_list(values1)
    second = create_linked_list(values2)

    print("First number:")
    print_linked_list(first)
    print("Second number:")
    print_linked_list(second)

    ops = LinkedListOps()
    result = ops.addTwoLists(first, second)

    print("Sum:")
    print_linked_list(result)

if __name__ == "__main__":
    main()
