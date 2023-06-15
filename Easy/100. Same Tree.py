class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def inorder_traversal(root: TreeNode):
        if root is None:
            return []

        inorder = []
        if root.left:
            inorder += inorder_traversal(root.left)
        else:
            inorder.append(None)

        inorder.append(root.val)

        if root.right:
            inorder += inorder_traversal(root.right)
        else:
            inorder.append(None)

        return inorder

    return inorder_traversal(p) == inorder_traversal(q)


def inorder_traversal(root: TreeNode):
    if root is None:
        return []

    inorder = []
    if root.left:
        inorder += inorder_traversal(root.left)
    else:
        inorder.append(None)

    inorder.append(root.val)

    if root.right:
        inorder += inorder_traversal(root.right)
    else:
        inorder.append(None)

    return inorder


if __name__ == '__main__':
    node1 = TreeNode(1, TreeNode(1))
    node2 = TreeNode(1, None, TreeNode(1))
    print(inorder_traversal(node1), inorder_traversal(node2))
