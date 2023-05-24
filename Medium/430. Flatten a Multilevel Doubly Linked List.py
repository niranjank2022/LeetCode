class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node) -> Node:
    curr = head
    while curr:
        if curr.child:
            next = curr.next
            child = curr.child
            curr.next, child.prev = child, curr

            flatten(child)

            while curr.next:
                curr = curr.next
            curr.next, next.prev = next, curr

        curr = curr.next

    return head
