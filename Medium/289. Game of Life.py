def gameOfLife(board: list[list[int]]) -> None:
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            count = 0
            for change in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= i + change[0] < m and 0 <= j + change[1] < n and board[i + change[0]][j + change[1]] % 2:
                    count += 1

            if board[i][j] == 0 and count == 3:
                board[i][j] += 2
            elif board[i][j] == 1 and (count == 2 or count == 3):
                board[i][j] += 2

    for i in range(m):
        for j in range(n):
            board[i][j] = 1 if board[i][j] > 1 else 0


if __name__ == '__main__':

    testcases = [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[1, 1], [1, 0]]]
    for case in testcases:
        print("*****")
        [print(row) for row in case]
        gameOfLife(case)
        print("\n")
        [print(row) for row in case]
        print("*****\n")
