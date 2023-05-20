class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head: ListNode | None = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < self.length:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.next
                i += 1
            return curr.data

    def addAtHead(self, val: int) -> None:

        self.head = ListNode(val, self.head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index <= self.length:
            prev = None
            curr = self.head
            i = 0
            while i < index:
                prev = curr
                curr = curr.next
                i += 1
            prev.next = ListNode(val, curr)
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        elif index < self.length:
            i = 0
            prev = None
            curr = self.head
            while i < index:
                prev = curr
                curr = curr.next
                i += 1
            prev.next = curr.next
        self.length -= 1
