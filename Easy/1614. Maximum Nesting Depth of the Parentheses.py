def maxDepth(s: str) -> int:
    stack = []
    max_depth = 0
    depth = 0
    for char in s:
        if char == '(':
            stack.append(char)
            depth += 1
        elif char == ')':
            stack.pop()
            if depth > max_depth:
                max_depth = depth
            depth -= 1

    return max_depth


if __name__ == '__main__':
    testcases = ["(1+(2*3)+((8)/4))+1", "(1)+((2))+(((3)))", "()(()())", "", "()()"]
    for case in testcases:
        print(f"{case} -> {maxDepth(case)}")
