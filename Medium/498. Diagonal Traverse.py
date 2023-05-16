def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    m = len(mat[0])
    n = len(mat)
    top_right = True
    bottom_left = False
    next_move = -1, 1
    x = y = 0
    answer = []

    while 0 <= x < n and 0 <= y < m:

        while top_right:
            answer.append(mat[x][y])
            if 0 <= x + next_move[0] < n and 0 <= y + next_move[1] < m:
                x, y = x + next_move[0], y + next_move[1]
            else:
                if y + 1 < m:
                    y = y + 1
                else:
                    x = x + 1
                top_right = False
                bottom_left = True

        while 0 <= x < n and 0 <= y < m and bottom_left:
            answer.append(mat[x][y])
            if 0 <= x - next_move[0] < n and 0 <= y - next_move[1] < m:
                x, y = x - next_move[0], y - next_move[1]
            else:
                if x + 1 < n:
                    x = x + 1
                else:
                    y = y + 1
                bottom_left = False
                top_right = True

    return answer


if __name__ == '__main__':
    testcases = [[[2, 3]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2], [3, 4]]]
    for case in testcases:
        print(f"{case} -> {findDiagonalOrder(case)}")
