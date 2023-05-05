def removeOuterParentheses(s: str) -> str:
    stack = []
    return_str = ""
    for char in s:
        if not stack:
            stack.append(char)

        else:
            if char == '(':
                stack.append(char)
                return_str += char
            elif char == ')':
                stack.pop()
                if stack:
                    return_str += char

    return return_str


if __name__ == '__main__':
    testcases = ["(()())(())", "(()())(())(()(()))", "()()"]
    for case in testcases:
        print(f"{case} -> \'{removeOuterParentheses(case)}\'")
