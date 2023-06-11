def decodeString(s: str) -> str:
    stack = []
    num, currString = 0, ""
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.extend((num, currString))
            num, currString = 0, ""
        elif ch == ']':
            prevString = stack.pop()
            num = stack.pop()
            currString = prevString + num * currString
            num = 0
        else:
            currString += ch

    return currString


if __name__ == '__main__':
    testcases = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for case in testcases:
        print(f"{case} -> {decodeString(case)}")
