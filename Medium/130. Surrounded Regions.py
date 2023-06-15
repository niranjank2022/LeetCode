import collections


def solve(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])

    def traverse(i, j):
        board[i][j] = '#'
        queue = collections.deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + move[0] < m and 0 <= y + move[1] < n and board[x + move[0]][y + move[1]] == 'O':
                    traverse(x + move[0], y + move[1])

    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                traverse(i, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'


if __name__ == '__main__':
    testcases = [[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]], [["X"]],
                 [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]]
    for case in testcases:
        print(f"{case}")
        solve(case)
        print(f"{case}")
