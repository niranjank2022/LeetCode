def generate(numRows: int) -> list[list[int]]:
    pascal = [[1]]

    for i in range(numRows - 1):
        row = [1]
        for i in range(1, len(pascal[-1])):
            row.append(pascal[-1][i - 1] + pascal[-1][i])
        row.append(1)
        pascal.append(row)

    return pascal


if __name__ == '__main__':

    testcases = [1, 3, 5, 4]
    for case in testcases:
        print(f"{case} -> {generate(case)}")
