import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



    def maxLevelSum(root: TreeNode) -> int:
        level, maxSum, maxLevel = 1, root.val, 1
        queue = collections.deque([root])
        while queue:
            sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum > maxSum:
                maxSum = sum
                maxLevel = level
            level += 1

        return maxLevel
