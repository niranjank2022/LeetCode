def smallestString(s: str) -> str:
    n = len(s)

    if n == s.count('a'):
        return s[:-1] + 'z'

    answer = ""
    ismodified = False
    for i in range(n):

        if s[i] == 'a' and ismodified:
            return answer + s[i:]
        elif s[i] == 'a':
            answer += 'a'
        else:
            answer += chr(ord(s[i]) - 1)
            ismodified = True

    return answer


if __name__ == '__main__':
    testcases = ["cbabc", "acbbc", "leetcode", "a", "ajsjbcb", "aab", "aaaafsa"]
    for case in testcases:
        print(f"{case} -> {smallestString(case)}")
