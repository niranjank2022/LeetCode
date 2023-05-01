def calPoints(operations: list[str]) -> int:
    stack = list()
    sum = 0
    for op in operations:
        if op == '+':
            sum += stack[-1] + stack[-2]
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            sum -= stack.pop()
        elif op == 'D':
            sum += 2 * stack[-1]
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
            sum += stack[-1]

    return sum


if __name__ == '__main__':
    testcases = [["5", "2", "C", "D", "+"], ["5", "-2", "4", "C", "D", "9", "+", "+"], ["1", "C"]]
    for case in testcases:
        print(f"{case} -> {calPoints(case)}")
