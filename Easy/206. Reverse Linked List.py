from random import randint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    curr, next = head, head.next

    while next:
        curr.next = next.next
        next.next = head
        head = next

        next = curr.next

    return head


"""
def reverseList(head: ListNode) -> ListNode:
    reverseNode = None
    while head is not None:
        reverseNode = ListNode(head.val, reverseNode)
        head = head.next

    return reverseNode
"""


def printList(node: ListNode):
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print("None")


def main():
    for _ in range(3):
        lst = [randint(0, 10) for _ in range(5)]
        node = None
        for i in lst:
            node = ListNode(i, node)
        print("\n\n")
        printList(node)

        printList(reverseList(node))


main()
