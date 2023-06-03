def lengthOfLongestSubstring(s: str) -> int:
    if s == "":
        return 0
    n = len(s)
    max_length = 1
    for i in range(n - 1):

        if s[i] == s[i + 1]:
            continue
        j = i
        hashset = set()
        while j < n and s[j] not in hashset:
            hashset.add(s[j])
            j += 1
        max_length = max(max_length, j - i)

    return max_length


if __name__ == '__main__':
    testcases = ["bbbbb", "abcabcbb", "pwwkew", "dvdf"]
    for case in testcases:
        print(f"{case} -> {lengthOfLongestSubstring(case)}")
