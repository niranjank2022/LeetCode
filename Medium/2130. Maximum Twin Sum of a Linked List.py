from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: ListNode) -> int:
    queue = deque()
    node1 = node2 = head

    # Traversing to the middle of the linked list
    while node2:
        queue.appendleft(node1.val)
        node1 = node1.next
        node2 = node2.next.next

    max_sum = - 1 << 63
    while node1:
        max_sum = max(max_sum, queue.popleft() + node1.val)
        node1 = node1.next

    return max_sum
