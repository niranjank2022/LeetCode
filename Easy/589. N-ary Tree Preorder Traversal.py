from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children: None | list[Node] = children


def preorder(root: Node) -> list[int]:
    preorder = list()
    if root:
        stack = deque()
        stack.append(root)
        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            if curr.children:
                stack.extend(reversed(curr.children))

    return preorder
