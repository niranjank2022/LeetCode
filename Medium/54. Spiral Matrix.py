def recursive_function(matrix: list[list[int]], horizontal_border: list[int], vertical_border: list[int]) -> list[int]:
    output = []

    if (horizontal_border[0] == horizontal_border[1]) and (vertical_border[0] == vertical_border[1]) and (
            horizontal_border[0] != vertical_border[0]):
        return output

    if horizontal_border[0] == horizontal_border[1]:
        for i in range(vertical_border[0], vertical_border[1] + 1):
            output.append(matrix[i][horizontal_border[0]])
        return output

    if vertical_border[0] == vertical_border[1]:
        for j in range(horizontal_border[0], horizontal_border[1] + 1):
            output.append(matrix[vertical_border[0]][j])
        return output

    i = vertical_border[0]
    j = horizontal_border[0]

    while j < horizontal_border[1]:
        output.append(matrix[i][j])
        j += 1

    if vertical_border[0] < vertical_border[1]:
        vertical_border[0] += 1
        while i < vertical_border[1]:
            output.append(matrix[i][j])
            i += 1

    if horizontal_border[0] < horizontal_border[1]:
        horizontal_border[1] -= 1
        while j > horizontal_border[0]:
            output.append(matrix[i][j])
            j -= 1

    if vertical_border[0] < vertical_border[1]:
        vertical_border[1] -= 1
        while i > vertical_border[0]:
            output.append(matrix[i][j])
            i -= 1

    if horizontal_border[0] < horizontal_border[1]:
        horizontal_border[0] += 1

    output.append(matrix[i][j])

    return output + recursive_function(matrix, horizontal_border, vertical_border)


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])

    horizontal_border = [0, n - 1]
    vertical_border = [0, m - 1]
    return recursive_function(matrix, horizontal_border, vertical_border)



if __name__ == '__main__':
    testcases = [[[2, 5], [8, 4], [0, -1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[3], [2]],
                 [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]], [[2, 5, 8], [4, 0, -1]]]
    for case in testcases:
        print(f"{case} -> {spiralOrder(case)}")
