def countNegatives(grid: list[list[int]]) -> int:
    count = 0
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] < 0:
                count += n - j
                break

    return count


if __name__ == '__main__':
    testcases = [[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], [[3, 2], [1, 0]]]
    for case in testcases:
        print(f"{case} -> {countNegatives(case)}")
