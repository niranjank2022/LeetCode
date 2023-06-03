class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.limit = k
        self.filled = 0

    def insertFront(self, value: int) -> bool:
        if self.filled == self.k:
            return False
        if self.head is None:
            self.head = self.tail = Node(value)

        else:
            self.head = Node(value, next=self.head)

    def insertLast(self, value: int) -> bool:

    def deleteFront(self) -> bool:

    def deleteLast(self) -> bool:

    def getFront(self) -> int:

    def getRear(self) -> int:

    def isEmpty(self) -> bool:

    def isFull(self) -> bool:
