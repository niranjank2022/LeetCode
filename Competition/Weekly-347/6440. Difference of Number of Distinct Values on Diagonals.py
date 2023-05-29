def differenceOfDistinctValues(grid: list[list[int]]) -> list[list[int]]:
    m, n = len(grid), len(grid[0])
    answer = [[] for _ in range(m)]

    # print(answer, m, n)
    for i in range(m):
        for j in range(n):

            topleft = bottomright = 0
            # Finding for top left
            x, y = i, j
            distinct = set()
            while 0 <= x - 1 < m and 0 <= y - 1 < n:
                x, y = x - 1, y - 1
                if grid[x][y] not in distinct:
                    topleft += 1
                    distinct.add(grid[x][y])

            # Finding for bottom right
            x, y = i, j
            distinct.clear()
            while 0 <= x + 1 < m and 0 <= y + 1 < n:
                x, y = x + 1, y + 1
                if grid[x][y] not in distinct:
                    bottomright += 1
                    distinct.add(grid[x][y])

            answer[i].append(abs(topleft - bottomright))

    return answer


if __name__ == '__main__':
    testcases = [[[1, 2, 3], [3, 1, 5], [3, 2, 1]], [[1]],
                 [[5, 50, 39, 37], [2, 19, 36, 26], [27, 3, 23, 10], [20, 33, 8, 39]]]
    for case in testcases:
        print(f"{case} -> {differenceOfDistinctValues(case)}")
