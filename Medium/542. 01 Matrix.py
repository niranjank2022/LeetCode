import collections
import sys

INT_MAX = sys.maxsize


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    dist = [[INT_MAX for _ in range(n)] for _ in range(m)]

    queue = collections.deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + x < m and 0 <= c + y < n and dist[r + x][c + y] > dist[r][c] + 1:
                dist[r + x][c + y] = dist[r][c] + 1
                queue.append((r + x, c + y))

    return dist


if __name__ == '__main__':
    testcases = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
                 [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                  [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]],

                 [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                  [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                  [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                  [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]

                 ]
    for case in testcases:
        print(f"{case} \n-> {updateMatrix(case)}")
