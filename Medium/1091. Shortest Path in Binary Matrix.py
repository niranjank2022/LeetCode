def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    if grid[0][0] == 1:
        return -1
    n = len(grid)
    i = j = 0
    dp = [[n * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if grid[i][j] == 1:
                continue

            if i == 0 and j == 0 and grid[i][j] == 0:
                dp[i][j] = 1
            elif i == 0 and grid[i][j - 1] == 0:
                dp[i][j] = dp[i][j - 1] + 1
            elif j == 0 and grid[i - 1][j] == 0:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp[n - 1][n - 1]


if __name__ == '__main__':
    testcases = [[[0, 1], [1, 0]], [[0, 0, 0], [1, 1, 0], [1, 1, 0]]]
    for case in testcases:
        print(f"{case} -> {shortestPathBinaryMatrix(case)}")
