class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    while head and head.val == val:
        head = head.next
    if head is None or head.next is None:
        return None

    prev, curr = head, head.next
    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = curr.next
            continue
        prev = curr
        curr = curr.next

    return head
