def getRow(rowIndex: int) -> list[int]:
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]

    last_row = [1, 1]
    for r in range(3, rowIndex + 2):
        row = []
        for i in range(r):
            if i == 0 or i == r - 1:
                row.append(1)
            else:
                row.append(last_row[i] + last_row[i - 1])

        last_row = row

    return last_row


if __name__ == '__main__':
    testcases = [3, 0, 1, 6]
    for case in testcases:
        print(f"{case} -> {getRow(case)}")
