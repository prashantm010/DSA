class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def intersectPoint(head1, head2):
    # Step 1: Find the lengths of both linked lists
    c1 = 0
    current1 = head1
    while current1:
        c1 += 1
        current1 = current1.next
        
    c2 = 0
    current2 = head2
    while current2:
        c2 += 1
        current2 = current2.next
    
    # Step 2: Calculate the difference in lengths
    diff = abs(c1 - c2)
    
    # Step 3: Align the starting points of both lists
    current1 = head1
    current2 = head2
    if c1 > c2:
        for _ in range(diff):
            current1 = current1.next
    else:
        for _ in range(diff):
            current2 = current2.next
    
    # Step 4: Traverse both lists together to find intersection point
    while current1 and current2:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next
    
    return None  # No intersection found

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
    # Example: Create two linked lists with an intersection
    list1 = list(map(int, input("Enter sorted list 1 (space-separated): ").split()))
    list2 = list(map(int, input("Enter sorted list 2 (space-separated): ").split()))
    
    head1 = create_linked_list(list1)
    head2 = create_linked_list(list2)
    
    # Manually creating intersection at node with value 4
    current1 = head1
    while current1 and current1.next:
        current1 = current1.next
    current2 = head2
    while current2 and current2.next:
        current2 = current2.next
    current2.next = current1.next.next  # Intersection at value 4

    print("List 1:")
    print_linked_list(head1)
    
    print("List 2:")
    print_linked_list(head2)
    
    intersection = intersectPoint(head1, head2)
    if intersection:
        print(f"Intersection at node with value: {intersection}")
    else:
        print("No intersection found")

if __name__ == "__main__":
    main()
