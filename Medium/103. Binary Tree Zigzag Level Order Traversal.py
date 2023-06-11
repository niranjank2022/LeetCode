import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return None

    queue = collections.deque([root])
    zigzag = []
    left_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node is None:
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_right:
            level = level.reverse()
        zigzag.append(level)
        left_right = not left_right

    return zigzag
