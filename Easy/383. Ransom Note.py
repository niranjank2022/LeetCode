def canConstruct(ransomNote: str, magazine: str) -> bool:
    for i in range(len(ransomNote)):
        if ransomNote[i] != magazine[i]:
            return False
    return True


if __name__ == '__main__':
    testcases = [("a", "b"), ("aa", "ab"), ("aa", "aab")]
    for case in testcases:
        print(f"{case} -> {canConstruct(case[0], case[1])}")
