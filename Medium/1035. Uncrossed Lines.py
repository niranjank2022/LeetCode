def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    n1, n2 = len(nums1), len(nums2)
    table = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    return table[n1][n2]


if __name__ == '__main__':
    testcases = [([1, 1, 3, 5, 3, 3, 5, 5, 1, 1],
                  [2, 3, 2, 1, 3, 5, 3, 2, 2, 1]), ([1, 4, 2], [1, 2, 4]), ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]),
                 ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1])]
    for case in testcases:
        print(f"{case} -> {maxUncrossedLines(case[0], case[1])}")
