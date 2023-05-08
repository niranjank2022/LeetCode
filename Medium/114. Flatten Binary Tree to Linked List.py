class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> list[TreeNode]:
    if not root:
        return []
    nodes = [root]
    if root.left:
        nodes += preorder_traversal(root.left)
    if root.right:
        nodes += preorder_traversal(root.right)

    return nodes


def flatten(root: TreeNode) -> None:
    nodes = preorder_traversal(root)
    curr: TreeNode = None
    for node in nodes:
        if curr is None:
            curr = node
        else:
            curr.right = node
            curr.left = None
            curr = curr.right


if __name__ == '__main__':
    node1 = TreeNode(2, TreeNode(3), TreeNode(4))
    node2 = TreeNode(5, right=TreeNode(6))
    tree = TreeNode(1, node1, node2)

