from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Preorder traversal - visits root node, left subtree and right subtree
# Recursive approach
def preorderTraversal1(root: TreeNode) -> list[int]:
    return [root.val, *preorderTraversal1(root.left), *preorderTraversal1(root.right)] if root else []


# Iterative approach
def preorderTraversal2(root: TreeNode) -> list[int]:
    preorder = list()

    if root:
        stack = deque()
        stack.append(root)
        while stack:

            curr = stack.pop()
            preorder.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    return preorder


def main():
    root = TreeNode()
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print(preorderTraversal1(root))
    print(preorderTraversal2(root))


main()
