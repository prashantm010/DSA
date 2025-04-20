class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListOps:
    def removeLoop(self, head):
        if head is None or head.next is None:
            return

        slow = head
        fast = head

        # Step 1: Detect loop using Floyd's Cycle Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # No loop found
        if slow != fast:
            return

        # Step 2: Count loop length
        loop_length = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            loop_length += 1

        # Step 3: Fix fast and slow to find start of loop
        slow = head
        fast = head
        for _ in range(loop_length):
            fast = fast.next

        # Step 4: Move both pointers until fast.next == slow
        while fast.next != slow:
            slow = slow.next
            fast = fast.next

        # Step 5: Break the loop
        fast.next = None

    def detectLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    nodes = [head]
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
        nodes.append(current)
    return head, nodes

def create_loop(head, nodes, pos):
    if pos == -1:
        return
    last = nodes[-1]
    loop_node = nodes[pos]
    last.next = loop_node

def print_linked_list(head):
    visited = set()
    while head:
        if head in visited:
            print(f"{head.data} -> ... (loop detected)")
            return
        print(head.data, end=" -> ")
        visited.add(head)
        head = head.next
    print("None")

def main():
    values = list(map(int, input("Enter elements (space-separated): ").split()))
    loop_pos = int(input("Enter loop position (0-indexed, -1 for no loop): "))

    head, nodes = create_linked_list(values)
    create_loop(head, nodes, loop_pos)

    ops = LinkedListOps()

    print("Before removing loop:")
    if ops.detectLoop(head):
        print("Loop detected!")
    else:
        print("No loop detected.")

    ops.removeLoop(head)

    print("\nAfter removing loop:")
    if ops.detectLoop(head):
        print("Loop still present!")
    else:
        print("Loop successfully removed.")
        print("Linked List:")
        print_linked_list(head)

if __name__ == "__main__":
    main()
