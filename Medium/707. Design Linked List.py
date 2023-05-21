class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


'''class MyLinkedList:

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
'''


class MyLinkedList:

    def __init__(self):
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < self.length:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.next
                i += 1
            return curr.data
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.tail = ListNode(val)
        else:
            # self.head = self.head.prev = ListNode(val, next=self.head)
            node = ListNode(val, next=self.head)
            self.head.prev = node
            self.head = node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = self.head = ListNode(val)
        else:
            # self.tail = self.tail.next = ListNode(val, prev=self.tail)
            node = ListNode(val, prev=self.tail)
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            curr = self.head
            i = 0
            while i != index:
                curr = curr.next
                i += 1
            # curr.prev = curr.prev.next = ListNode(val, curr.prev, curr)
            prev = curr.prev
            prev.next = curr.prev = ListNode(val, prev, curr)
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 == self.length - 1:
            self.head = self.tail = None
            self.length -= 1
        elif 0 <= index < self.length:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif index == self.length - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            elif index < self.length:
                i = 0
                curr = self.head
                while i != index:
                    curr = curr.next
                    i += 1
                curr.prev.next, curr.next.prev = curr.next, curr.prev
            self.length -= 1


def printNodes(head: MyLinkedList):
    curr = head.head
    print(f"Head: {head.head} Tail: {head.tail} Length: {head.length}")
    while curr:
        print(curr.data, end='-> ')
        curr = curr.next
    print(None, end='\n\n')


if __name__ == '__main__':
    list1 = MyLinkedList()
    printNodes(list1)

    list1.addAtTail(1)
    printNodes(list1)

    list1.addAtTail(2)
    printNodes(list1)

    list1.addAtTail(3)
    printNodes(list1)

    list1.addAtHead(0)
    list1.addAtHead(-1)
    printNodes(list1)

    list1.addAtIndex(2, 0.4)
    printNodes(list1)

    # for i in range(list1.length):
    #     print(list1.get(i))

    list1.deleteAtIndex(2)
    printNodes(list1)

    list1.deleteAtIndex(0)
    printNodes(list1)

    list1.addAtTail(6)
    list1.addAtIndex(6, 89)
    printNodes(list1)
