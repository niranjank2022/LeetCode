def tribonacci(n: int) -> int:
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]


if __name__ == '__main__':
    testcases = [0, 1, 2, 3, 4, 25]
    for case in testcases:
        print(f"{case} -> {tribonacci(case)}")
