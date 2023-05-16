def removeDuplicateLetters(s: str) -> str:
    chars = list(s)
    chars.sort()
    answer = chars[0]
    for i in range(1, len(chars)):
        if chars[i] != chars[i - 1]:
            answer += chars[i]

    return answer


if __name__ == '__main__':
    testcases = ["bcabc", "cbacdcbc"]
    for case in testcases:
        print(f"{case} -> {removeDuplicateLetters(case)}")
