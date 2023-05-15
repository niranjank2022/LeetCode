class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: ListNode, k: int) -> ListNode:
    # Finding the length of linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    if length == 1:
        return head

    # Finding the required nodes
    node1 = node2 = None
    curr = head
    i = 1
    while curr:
        if i == k:
            node1 = curr
        if i == length - k + 1:
            node2 = curr
        i += 1
        curr = curr.next

    # Swapping them
    node1.val, node2.val = node2.val, node1.val
    return head
