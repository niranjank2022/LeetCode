class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def main():
    node1 = ListNode()
    node1.next = ListNode(1)
    head = node1.next
    node1.next.next = ListNode(2)
    node1.next.next.next = ListNode(3)
    node1.next.next.next.next = ListNode(4)
    node1.next.next.next.next.next = head
    # printList(node1)        # Caution: This  will print the cycly linked list leading to infinite printing of values

    head = node1

    slow = node1.next
    fast = node1.next.next
    count = 1
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        print(count)
        count += 1

    print(f"Head of the list: {head.val}")
    print(f"Node of intersection: {slow.val} count: {count}")

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    print(f"The cycle starts at {slow.val}")


main()
