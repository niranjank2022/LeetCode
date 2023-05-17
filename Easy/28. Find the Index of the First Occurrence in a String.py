def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1


def main():
    testcases = [("mississippi", "issipi"), ("salbutsad", "sad"), ("leetcode", "leeto"), ("appy", "appy")]
    for case in testcases:
        print(f"{case} -> {strStr(case[0], case[1])}")


main()
