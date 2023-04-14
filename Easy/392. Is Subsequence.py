def isSubsequence(s: str, t: str) -> bool:
    j = -1
    for i in s:
        try:
            j = t.index(i, j+1)
        except ValueError:
            return False

    return True


def main():
    testcases = [["abc", "ahbgdc"], ["ace", "abcde"], ["aec", "abcde"], ["aaaaaa", "bbaaaa"]]
    for case in testcases:
        print(f"'{case}' ~ {isSubsequence(case[0], case[1])}")
        print("===============")


main()
