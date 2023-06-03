class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:

    if not root:
        return True
    if root.left:
        if root.left.val > root.val:
            return False
        else:
            return isValidBST(root.left)







