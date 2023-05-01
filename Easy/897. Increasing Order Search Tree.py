class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        left = None
        curr = root
        elements = self.inorder_traversal(root)
        while curr.left:
            curr = curr.left

        left = curr
        curr = left

        elements = self.inorder_traversal(root)
        i = 1
        while i < len(elements):
            curr.right = TreeNode(elements[i])
            curr = curr.right
            i += 1

        return left

    def inorder_traversal(self, root: TreeNode) -> list:
        inorder = []
        if root.left:
            inorder += self.inorder_traversal(root.left)

        inorder.append(root.val)

        if root.right:
            inorder += self.inorder_traversal(root.right)

        return inorder
