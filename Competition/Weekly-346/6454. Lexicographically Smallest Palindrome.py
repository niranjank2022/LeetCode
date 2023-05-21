def makeSmallestPalindrome(s: str) -> str:
    n = len(s)
    answer = list(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if answer[n - i - 1] > answer[i]:
                answer[n - 1 - i] = answer[i]
            elif answer[i] > answer[n - i - 1]:
                answer[i] = answer[n - 1 - i]

    return "".join(answer)


if __name__ == '__main__':

    testcases = ["ABFCACDB", "ACBBD"]
    for case in testcases:
        print(f"{case} -> {makeSmallestPalindrome(case)}")
