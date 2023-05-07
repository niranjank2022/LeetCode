from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode) -> None:
    stack = deque()
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    ordered_stack = deque()
    while stack:
        ordered_stack.append(stack.popleft())
        if stack:
            ordered_stack.append(stack.pop())

    curr = head
    for node in ordered_stack[1:]:
        curr.next = node

    curr.next = None
