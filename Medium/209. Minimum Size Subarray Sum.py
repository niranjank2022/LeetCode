def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    sum = left = 0
    ans = (1 << 31) - 1
    for i in range(n):
        sum += nums[i]
        while sum >= target:
            ans = min(ans, i - left + 1)
            sum -= nums[left]
            left += 1

    return ans if ans != (1 << 31) - 1 else 0


if __name__ == '__main__':
    testcases = [(7, [2, 3, 1, 2, 4, 3]), (11, [1, 1, 1, 1, 1, 1, 1, 1]), (4, [1, 4, 4])]
    for case in testcases:
        print(f"{case} -> {minSubArrayLen(case[0], case[1])}")
