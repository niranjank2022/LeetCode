def isValid(s: str) -> bool:
    stack = [s[0]]
    parentheses = {')': '(', ']': '[', '}': '{'}
    for i in s[1::]:
        if stack and parentheses.get(i) == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return stack == []


if __name__ == '__main__':
    testcases = ["()", "()[]{}", "(]", "}", "{[()]}{}", "(])"]
    for case in testcases:
        print(f"\'{case}\' -> {isValid(case)}")
