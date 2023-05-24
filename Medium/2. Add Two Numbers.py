class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    head1, head2 = l1, l2
    while l1 and l2:
        l1.val, l2.val, carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) % 10, (
                l1.val + l2.val + carry) // 10
        if l1.next is None and l2.next is None:
            if carry == 1:
                l1.next = ListNode(carry)
            return head1
        l1, l2 = l1.next, l2.next

    while l1:
        l1.val, carry = (l1.val + carry) % 10, (l1.val + carry) / 10
        if l1.next is None:
            if carry == 1:
                l1.next = ListNode(1)
            return head1
        l1 = l1.next

    while l2:
        l2.val, carry = (l2.val + carry) % 10, (l2.val + carry) / 10
        if l2.next is None:
            if carry == 1:
                l2.next = ListNode(carry)
            return head2
        l2 = l2.next

'''
[9,9,9,9,9,9,9]
[9,9,9,9]

8,9,9,9,0,0,0,1
'''