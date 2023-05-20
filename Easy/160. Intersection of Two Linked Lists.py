class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    node1 = headA
    node2 = headB

    while node1 != node2:
        node1 = headB if node1 is None else node1.next
        node2 = headA if node2 is None else node2.next
    return node1
