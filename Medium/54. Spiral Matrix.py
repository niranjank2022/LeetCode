def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    x = y = 0
    vertical_border, horizontal_border = [0, m], [0, n]
    direction, next_move = 0, (1, 1, -1, -1)
    answer = []

    while vertical_border[0] <= x < vertical_border[1] and horizontal_border[0] <= y < horizontal_border[1]:

        while direction == 0 and vertical_border[0] <= x < vertical_border[1] and horizontal_border[0] <= y < \
                horizontal_border[1]:  # Moving right
            answer.append(matrix[x][y])
            if horizontal_border[0] <= y + next_move[direction] < horizontal_border[1]:
                y += next_move[direction]
            else:
                direction = 1
                x += next_move[direction]
                vertical_border[0] += 1

        while direction == 1 and vertical_border[0] <= x < vertical_border[1] and horizontal_border[0] <= y < \
                horizontal_border[1]:  # Move downward
            answer.append(matrix[x][y])
            if vertical_border[0] <= x + next_move[direction] < vertical_border[1]:
                x += next_move[direction]
            else:
                direction = 2
                y += next_move[direction]
                horizontal_border[1] -= 1

        while direction == 2 and vertical_border[0] <= x < vertical_border[1] and horizontal_border[0] <= y < \
                horizontal_border[1]:  # Move leftward
            answer.append(matrix[x][y])
            if horizontal_border[0] <= y + next_move[direction] < horizontal_border[1]:
                y += next_move[direction]
            else:
                direction = 3
                x += next_move[direction]
                vertical_border[1] -= 1

        while direction == 3 and vertical_border[0] <= x < vertical_border[1] and horizontal_border[0] <= y < \
                horizontal_border[1]:  # Move upward
            answer.append(matrix[x][y])
            if vertical_border[0] <= x + next_move[direction] < vertical_border[1]:
                x += next_move[direction]
            else:
                direction = 0
                y += next_move[direction]
                horizontal_border[0] += 1

    return answer


if __name__ == '__main__':
    testcases = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [[2, 5], [8, 4], [0, -1]],
                 [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[3], [2]],
                 [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]], [[2, 5, 8], [4, 0, -1]]]
    for case in testcases:
        print(f"{case} -> {spiralOrder(case)}")
