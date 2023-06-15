class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: TreeNode) -> int:
    def inorder_traversal(node: TreeNode) -> list[int]:
        if node is None:
            return []

        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    nums = inorder_traversal(root)
    answer = nums[-1]
    for i in range(len(nums) - 1):
        answer = min(answer, nums[i + 1] - nums[i])
    return answer
