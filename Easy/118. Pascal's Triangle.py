def generate(numRows: int) -> list[list[int]]:
    pascal = [[1]]
    if numRows >= 2:
        pascal.append([1, 1])
    if numRows >= 3:
        for i in range(2, numRows):
            lst = [1]
            for j in range(i - 1):
                lst.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            lst.append(1)
            pascal.append(lst)

    return pascal


def main():
    testcases = [5, 1, 4, 2]
    for case in testcases:
        print(case)
        [print(i) for i in generate(case)]
        print("################")



main()
