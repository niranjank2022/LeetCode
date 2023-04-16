from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Post Order Traversal - visits root node, right subtree and then the left subtree
# Recursive approach
def postorderTraversal1(root: TreeNode) -> list[int]:
    return [*postorderTraversal1(root.left), *postorderTraversal1(root.right), root.val] if root else []


# Iterative approach
def postorderTraversal2(root: TreeNode) -> list[int]:
    postorder = list()
    if root:
        stack = deque()
        stack.append(root)
        while stack:
            curr = stack.pop()
            postorder.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

    postorder.reverse()
    return postorder


def main():
    root = TreeNode()
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print(postorderTraversal1(root))
    print(postorderTraversal2(root))


main()
