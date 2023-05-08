def diagonalSum(mat: list[list[int]]) -> int:
    order = len(mat)
    diagonal_sum = 0
    for i in range(order):
        diagonal_sum += mat[i][i]
        diagonal_sum += mat[i][order - i - 1]

    if order % 2 == 1:  # If order is odd, then there is a common element between the primary as well as secondary diagonal
        diagonal_sum -= mat[order // 2][order // 2]

    return diagonal_sum


if __name__ == '__main__':
    testcases = [[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], [[1, 1, 1, 1],
                               [1, 1, 1, 1],
                               [1, 1, 1, 1],
                               [1, 1, 1, 1]], [[5]]]
    for case in testcases:
        print(f"{case} -> {diagonalSum(case)}")
