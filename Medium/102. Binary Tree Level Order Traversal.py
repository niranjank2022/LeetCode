from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    levelorder = list()
    if root:
        stack = deque()

        stack.append(root)
        while stack:
            level = list()
            for _ in range(len(stack)):
                curr = stack.popleft()
                level.append(curr.val)

                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

            levelorder.append(level)

        return levelorder


def main():
    root = TreeNode()
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print(levelOrder(root))
    # print(preorderTraversal2(root))


main()
