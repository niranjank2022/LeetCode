def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])

    return traverse_matrix(matrix, [0, m], [0, n])


def traverse_matrix(matrix: list[list[int]], vertical_border: list[int], horizontal_border: list[int]):
    output = []
    m = vertical_border[1] - vertical_border[0]
    n = horizontal_border[1] - horizontal_border[0]

    if m <= 0 or n <= 0:
        return output

    if n == 1:
        for y in range(vertical_border[0], vertical_border[1]):
            output.append(matrix[y][horizontal_border[0]])
        return output

    if m == 1:
        for x in range(horizontal_border[0], horizontal_border[1]):
            output.append(matrix[vertical_border[0]][x])
        return output

    curr_x = horizontal_border[0]
    curr_y = vertical_border[0]

    # Traverse till the right end
    for x in range(horizontal_border[0], horizontal_border[1]):
        curr_x = x
        output.append(matrix[curr_y][curr_x])
    output.pop()

    # Traverse till the bottom end
    for y in range(vertical_border[0], vertical_border[1]):
        curr_y = y
        output.append(matrix[curr_y][curr_x])
    output.pop()

    # Traverse till the  left end
    for x in reversed(range(horizontal_border[0], horizontal_border[1])):
        curr_x = x
        output.append(matrix[curr_y][curr_x])
    output.pop()

    # Traverse till the top end
    for y in reversed(range(vertical_border[0], vertical_border[1])):
        curr_y = y
        output.append(matrix[curr_y][curr_x])
    output.pop()

    horizontal_border[0] += 1
    horizontal_border[1] -= 1
    vertical_border[0] += 1
    vertical_border[1] -= 1

    return output + traverse_matrix(matrix, vertical_border, horizontal_border)


if __name__ == '__main__':
    testcases = [[[2, 5], [8, 4], [0, -1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[3], [2]],
                 [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]], [[2, 5, 8], [4, 0, -1]]]
    for case in testcases:
        print(f"{case} -> {spiralOrder(case)}")
