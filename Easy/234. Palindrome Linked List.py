class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode):
    if head is None:
        return False
    stack = list()
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next

    return stack == stack[::-1]
