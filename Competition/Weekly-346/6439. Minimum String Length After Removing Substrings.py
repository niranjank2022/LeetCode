def minLength(s: str) -> int:
    stack = []
    for char in s:
        if stack and ((char == 'B' and stack[-1] == 'A') or (char == 'D' and stack[-1] == 'C')):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


if __name__ == '__main__':

    testcases = ["ABFCACDB", "ACBBD"]
    for case in testcases:
        print(f"{case} -> {minLength(case)}")
