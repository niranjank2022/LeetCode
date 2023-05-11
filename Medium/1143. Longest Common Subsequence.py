def longestCommonSubsequence(text1: str, text2: str) -> int:

    n1, n2 = len(text1), len(text2)
    table = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n1][n2]


if __name__ == '__main__':

    testcases = [("ezupkr", "ubmrapg"), ("abcde", "ade"), ("abc", "def")]
    for case in testcases:
        print(f"{case} -> {longestCommonSubsequence(case[0], case[1])}")
