def removeDuplicates(s: str) -> str:
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


if __name__ == '__main__':
    testcases = ["abbaca", "azxxzy"]
    for case in testcases:
        print(f"{case} -> \'{removeDuplicates(case)}\'")
