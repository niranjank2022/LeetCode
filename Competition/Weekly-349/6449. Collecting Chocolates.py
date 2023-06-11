import collections


def minCost(nums: list[int], x: int) -> int:
    n = len(nums)
    types = collections.deque([i for i in range(0, n)])
    collected = set()
    cost = 0
    for i in range(n):
        if i < x:
            cost += nums[i]
            collected.add(i)

    for i in range(n):
        if i >= 