def findTargetSumWays(nums: list[int], target: int) -> int:
    n = len(nums)
    memo = [{} for _ in range(n)]

    def calculate(i=0, sum=0):
        if i == n:
            return 1 if sum == target else 0
        else:
            if memo[i].get(sum) is None:
                memo[i][sum] = calculate(i + 1, sum + nums[i]) + calculate(i + 1, sum - nums[i])
                return memo[i][sum]
            else:
                return memo[i][sum]

    return calculate(0, 0)


if __name__ == '__main__':
    testcases = [([1, 1, 1, 1, 1], 3), ([1], 1),
                 ([25, 14, 16, 44, 9, 22, 15, 27, 23, 10, 41, 25, 14, 35, 28, 47, 39, 26, 11, 38], 43),
                 ([35, 16, 11, 38, 44, 5, 17, 20, 23, 0, 27, 46, 38, 29, 22, 18, 27, 34, 12, 10], 22),
                 ([0, 17, 5, 0, 0, 18, 18, 28, 36, 29, 42, 4, 32, 2, 5, 31, 24, 30, 8, 6], 27)]
    for case in testcases:
        print(f"{case} -> {findTargetSumWays(case[0], case[1])}")
