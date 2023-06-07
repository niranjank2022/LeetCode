def checkStraightLine(coordinates: list[list[int]]) -> bool:
    n = len(coordinates)
    if n == 2:
        return True

    slope = 1
    for i in range(1, len(coordinates)):
        if i == 1:
            if coordinates[i][0] - coordinates[i - 1][0] == 0:
                slope = 'undefined'
            else:
                slope = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
        else:

            if coordinates[i][0] - coordinates[i - 1][0] == 0:
                if slope != 'undefined':
                    return False
            elif (coordinates[i][1] - coordinates[i - 1][1]) / (
                    coordinates[i][0] - coordinates[i - 1][0]) != slope:
                return False

    return True


if __name__ == '__main__':
    testcases = [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]],
                 [[0, 0], [0, 1], [0, -1]]]
    for case in testcases:
        print(f"{case} -> {checkStraightLine(case)}")
