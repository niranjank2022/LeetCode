class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if k == 0 or head is None or head.next is None:
        return head

    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1

    if k % length == 0:
        return head

    curr = head
    for _ in range(length - k % length - 1):
        curr = curr.next

    new_head, curr.next = curr.next, None
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head

    return new_head
