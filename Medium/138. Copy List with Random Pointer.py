class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandom(head: Node) -> Node:
    if head is None:
        return head

    curr = head
    prev = None
    while curr:
        if prev:
            prev.next = Node(prev.val, curr)

        prev = curr
        curr = curr.next

    if prev:
        prev.next = Node(prev.val, curr)

    prev = head
    curr = head.next
    head = curr
    while curr:
        curr.random = prev.random.next if prev.random is not None else None

        if curr.next is None:
            break
        prev = prev.next.next
        curr.next = prev.next
        curr = curr.next

    return head


if __name__ == '__main__':
    n5 = Node(1)
    n4 = Node(10, n5)
    n3 = Node(11, n4)
    n2 = Node(13, n3)
    n1 = Node(7, n2)

    n1.random = None
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    copyRandom(n1)
'''

7 - 7 - 13 - 13 - 11 - 11 - 10 - 10 - 1 - 1 - None
N       7         1         11        7 

7 - 13 - 11 - 10 - 1 -  
N   7    1    11   7
'''
