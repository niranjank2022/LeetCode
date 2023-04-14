import time

class ListNode:
    def __init__(self, data, node):
        self.data = data
        self.next = node


def printList(node: ListNode):
    while node is not None:
        print(node.data, end=' -> ')
        node = node.next
    print("None")


def mergeTwoLists(node1: ListNode, node2: ListNode) -> ListNode:
    lst = list()
    while node1 is not None:
        lst.append(node1.data)
        node1 = node1.next
    while node2 is not None:
        lst.append(node2.data)
        node2 = node2.next

    sortednode: ListNode | None = None
    for i in sorted(lst, reverse=True):
        sortednode = ListNode(i, sortednode)

    return sortednode


def main():
    list1 = None
    list2 = None
    for i in range(5, 0, -1):
        list1 = ListNode(i * 2, list1)
        list2 = ListNode(i * 3, list2)

    printList(list1)
    printList(list2)

    start = time.clock()
    printList(mergeTwoLists(list1, list2))
    start = time.clock() - start

    print(f"Time taken is  {start} sec")


main()
