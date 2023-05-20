class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head1: ListNode) -> ListNode:
    if head1 is None or head1.next is None or head1.next.next is None:
        return head1

    head2 = head1.next
    curr1, curr2 = head1, head2

    while curr1 and curr2:
        curr1.next = curr2.next
        if curr1.next is None:
            break
        curr1 = curr1.next
        if curr1:
            curr2.next = curr1.next
            curr2 = curr2.next

    curr1.next = head2

    return head1
'''
1*--2*--3--4--None
1--3*--4--None
2--4*--None

1--3*--None
2--4*

1*--2*--3--4--5

1--3*--4--5--None
2--4*--5--None

1--3--5*--None
2--4--None

===

2*   1*   3   5   6   4   7   ||  2   3   6   7   1   5   4

2   3*   5   6   4   7
1   5*  6   4   7

2   3   6*  4   7
1   5   4*  7

2   3   6   7*  None
1   5   4   None

'''
