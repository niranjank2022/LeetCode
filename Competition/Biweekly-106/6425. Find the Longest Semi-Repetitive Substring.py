def longestSemiRepetitiveSubstring(s: str) -> int:
    n = len(s)
    if n == 1:
        return 1
    max_len = 0

    for i in range(n - 1):
        length = 1
        isSemiRepetitive = False
        for j in range(i + 1, n):

            if s[j] == s[j - 1]:
                if isSemiRepetitive:
                    length = max(length, j - i)
                    break
                isSemiRepetitive = True

            length = max(length, j - i + 1)
        max_len = max(max_len, length)
    return max_len


if __name__ == '__main__':
    testcases = ["1111111", "5494", "52233", "01", "123", "0001", "0010"]
    for case in testcases:
        print(f"{case} -> {longestSemiRepetitiveSubstring(case)}")
