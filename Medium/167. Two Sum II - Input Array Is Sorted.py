def minSubArrayLen(target: int, nums: list[int]) -> int:
    nums.sort()
    max_len = 0
    i = len(nums) - 1

    curr = 0
    while i >= 0 and curr < target:
        curr += nums[i]
        max_len += 1
        i -= 1

    return 0 if curr < target else max_len


if __name__ == '__main__':
    testcases = [(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]), (7, [2, 3, 1, 2, 4, 3]), (4, [1, 4, 4]),
                 (11, [1, 1, 1, 1, 1, 1, 1, 1])]
    for case in testcases:
        print(f"{case} -> {minSubArrayLen(case[0], case[1])}")
