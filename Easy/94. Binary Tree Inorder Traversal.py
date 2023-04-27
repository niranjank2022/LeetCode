class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(root) -> list[int]:
    inorder = []
    if root:
        if root.left:
            inorder += inOrderTraversal(root.left)

        inorder.append(root.data)

        if root.right:
            inorder += inOrderTraversal(root.right)

        return inorder
