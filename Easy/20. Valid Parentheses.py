def isValid(s: str) -> bool:
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            stack.append(char)

    return stack == []


if __name__ == '__main__':
    testcases = ["()", "()[]{}", "(]", "}", "{[()]}{}", "(])"]
    for case in testcases:
        print(f"\'{case}\' -> {isValid(case)}")
