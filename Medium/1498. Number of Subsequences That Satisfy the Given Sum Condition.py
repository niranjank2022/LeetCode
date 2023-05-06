def numSubseq(nums: list[int], target: int) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    res = 0
    mod = 10 ** 9 + 7
    while l <= r:
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            res += pow(2, r - l, mod)
            l += 1
    return res % mod


if __name__ == '__main__':
    testcases = [([3, 5, 6, 7], 9), ([3, 3, 6, 8], 10), ([2, 3, 3, 4, 6, 7], 12)]
    for case in testcases:
        print(f"{case} -> {numSubseq(case[0], case[1])}")
