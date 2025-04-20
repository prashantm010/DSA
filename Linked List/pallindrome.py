class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListOps:
    def reverseList(self, temp):  
        current = temp
        prevNode = None
      
        while current:  
            nextNode = current.next  
            current.next = prevNode  
            prevNode = current  
            current = nextNode  
        return prevNode  

    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count += 1  
            curr_node = curr_node.next
        return count

    def isPalindrome(self, head):  
        if not head or not head.next:
            return True
        
        size = self.getSize(head)
        mid = size // 2

        current = head
        for _ in range(mid - 1):
            current = current.next

        # For odd-size lists, skip the middle element
        if size % 2 != 0:
            current = current.next

        second_half_start = self.reverseList(current.next)
        first_half = head
        second_half = second_half_start

        result = True
        while second_half:
            if first_half.data != second_half.data:
                result = False
                break
            first_half = first_half.next
            second_half = second_half.next

        return result

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
    values = input("Enter elements of the list (space-separated): ").split()
    head = create_linked_list(values)

    print("Linked List:")
    print_linked_list(head)

    ops = LinkedListOps()
    if ops.isPalindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()
