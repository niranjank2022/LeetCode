def evalRPN(tokens: list[str]) -> int:
    numbers = []
    for char in tokens:
        if char.isdigit() or char[1:].isdigit():
            numbers.append(int(char))
        else:
            n2, n1 = numbers.pop(), numbers.pop()
            if char == '+':
                numbers.append(n1 + n2)
            elif char == '-':
                numbers.append(n1 - n2)
            elif char == '*':
                numbers.append(n1 * n2)
            else:
                numbers.append(int(n1 / n2))

    return numbers[-1]


if __name__ == '__main__':
    testcases = [["2", "1", "+", "3", "*"], ["4", "13", "5", "/", "+"],
                 ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
    for case in testcases:
        print(f"{case} -> {evalRPN(case)}")
