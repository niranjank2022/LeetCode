def evalRPN(tokens: list[str]) -> int:
    stack = []
    for char in tokens:
        if char.isdigit() or char[1:].isdigit():
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if char == '+':
                stack.append(num1 + num2)
            elif char == '-':
                stack.append(num1 - num2)
            elif char == '*':
                stack.append(num1 * num2)
            elif char == '/':
                stack.append(int(num1 / num2))

    return stack[0]


if __name__ == '__main__':
    testcases = [["2", "1", "+", "3", "*"], ["4", "13", "5", "/", "+"],
                 ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
    for case in testcases:
        print(f"{case} -> {evalRPN(case)}")
