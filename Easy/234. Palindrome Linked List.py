class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode):
    if head is None:
        return False
    node1 = node2 = head
    while node2 and node2.next and node2.next.next:
        node2 = node2.next.next
        node1 = node1.next

    node2 = node1.next
    node1.next = None

    node1 = head
    node2 = reverseList(node2)

    while node1 and node2:
        if node1.val != node2.val:
            return False
        node1, node2 = node1.next, node2.next
    return True


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
    if head is None:
        return False
    stack = list()
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next

    return stack == stack[::-1]
"""


def printNode(head: ListNode):
    while head:
        print(head.val, end='-> ')
        head = head.next
    print(None)


if __name__ == '__main__':
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    node2 = None

    printNode(node1)
    print(isPalindrome(node1))

    printNode(node2)
    print(isPalindrome(node2))
