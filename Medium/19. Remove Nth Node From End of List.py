class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    node1, curr, prev = head, head, None

    for i in range(n - 1):
        node1 = node1.next

    while node1.next:
        node1 = node1.next
        prev = curr
        curr = curr.next

    if curr == head:
        head = head.next
    else:
        prev.next = curr.next

    return head
