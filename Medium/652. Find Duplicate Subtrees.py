import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root: TreeNode) -> list[TreeNode]:
    def traverse(node: TreeNode):
        if node is None:
            return ""

        str_tree = '(' + traverse(node.left) + ')' + str(node.val) + '(' + traverse(node.right) + ')'

        duplicates[str_tree] += 1
        if duplicates[str_tree] == 2:
            answer.append(node)

        return str_tree

    duplicates = collections.defaultdict(int)
    answer = []
    traverse(root)
    return answer
