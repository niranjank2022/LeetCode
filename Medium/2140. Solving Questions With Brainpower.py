def mostPoints(questions: list[list[int]]) -> int:
    n = len(questions)
    array = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            array[i] = questions[i][0]
            continue

        j = i + questions[i][1] + 1
        if j < n and questions[i][0] + array[j] > array[i + 1]:
            array[i] = questions[i][0] + array[j]
        elif questions[i][0] > array[i + 1]:
            array[i] = questions[i][0]
        else:
            array[i] = array[i + 1]

    return array[0]


if __name__ == '__main__':
    testcases = [[[43, 5]], [[3, 2], [4, 3], [4, 4], [2, 5]], [[3, 2], [4, 3], [4, 4], [2, 5]],
                 [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                 [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]]

    for case in testcases:
        print(f"{case} -> {mostPoints(case)}")
