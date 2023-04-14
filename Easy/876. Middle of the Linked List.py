from random import randint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    length = 0
    current = head
    while current is not None:
        current = current.next
        length += 1

    print(length)
    length = length // 2
    while length > 0:
        head = head.next
        length -= 1

    return head


def printList(node: ListNode):
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print("None")


def main():
    for _ in range(3):
        lst = [randint(0, 10) for _ in range(randint(1, 10))]
        node = None
        for i in lst:
            node = ListNode(i, node)
        print("\n\n")
        printList(node)

        printList(middleNode(node))


main()
