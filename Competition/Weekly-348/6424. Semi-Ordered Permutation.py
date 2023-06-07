def semiOrderedPermutation(nums: list[int]) -> int:
    n = len(nums)
    if nums[0] == 1 and nums[-1] == n:
        return 0

    k = nums.index(1)
    answer = k

    for _ in range(k):
        nums[k], nums[k - 1] = nums[k - 1], nums[k]
        k -= 1

    return answer + n - 1 - nums.index(n)


if __name__ == '__main__':
    testcases = [[2, 1, 4, 3], [2, 4, 1, 3], [1, 3, 4, 2, 5]]
    for case in testcases:
        print(f"{case} -> {semiOrderedPermutation(case)}")
