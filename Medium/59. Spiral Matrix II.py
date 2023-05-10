def generateMatrix(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        matrix.append([0 for i in range(n)])

    # print(matrix)

    start = 0
    end = n
    val = 1

    while val <= n ** 2:

        curr_x = curr_y = start

        if end - start == 1:
            matrix[curr_y][curr_x] = val
            break
        # Traverse till the right end
        for x in range(start, end):
            curr_x = x
            matrix[curr_y][curr_x] = val
            val += 1
        val -= 1

        # Traverse till the  bottom end
        for y in range(start, end):
            curr_y = y
            matrix[curr_y][curr_x] = val
            val += 1
        val -= 1

        # Traverse till the left end
        for x in reversed(range(start, end)):
            curr_x = x
            matrix[curr_y][curr_x] = val
            val += 1
        val -= 1

        # Traverse till the top end
        for y in reversed(range(start + 1, end)):
            curr_y = y
            matrix[curr_y][curr_x] = val
            val += 1

        start += 1
        end -= 1

    return matrix


if __name__ == '__main__':
    testcases = [3, 4, 1, 2]
    for case in testcases:
        print(f"{case} -> {generateMatrix(case)}")
