def makeGood(s: str) -> str:
    stack = ['', s[0]]

    for char in s[1:]:
        if (char.islower() and stack[-1] == char.upper()) or (char.isupper() and stack[-1] == char.lower()):
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


if __name__ == '__main__':
    testcases = ["leEeetcode", "abBAcC", "s"]
    for case in testcases:
        print(f"{case} -> {makeGood(case)}")
