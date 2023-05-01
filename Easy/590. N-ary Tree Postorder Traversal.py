class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: Node) -> list[int]:
    if root is None:
        return []

    post_order = []
    if root.children:
        for child in root.children:
            post_order += postorder(child)

    post_order.append(root.val)

    return post_order
