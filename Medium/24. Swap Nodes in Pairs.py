class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    if head is None:
        return head

    curr = head
    next = curr.next

    while curr and next:
        if curr == head:
            curr.next, next.next = next.next, curr
            head = next
        else:
            curr.next, next.next = next.next, curr

        if curr.next and curr.next.next:
            next = curr.next
            curr.next = curr.next.next
            curr = next
            next = curr.next
        else:
            curr = curr.next
            if curr:
                next = curr.next

    return head


def printNodes(head: ListNode):
    curr = head
    while curr:
        print(curr.val, "->", end=' ')
        curr = curr.next
    print(None)


if __name__ == '__main__':
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node2 = None
    testcases = [node1, node2]
    for case in testcases:
        printNodes(case)
        printNodes(swapPairs(case))
