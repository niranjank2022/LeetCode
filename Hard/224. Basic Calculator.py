def infix_to_postfix(infix: str) -> list[str]:
    infix = "".join(infix.split())
    postfix = []
    stack = []
    prev_is_digit = False
    for index, char in enumerate(infix):
        if char.isdigit() and prev_is_digit:
            postfix[-1] += char
        elif char.isdigit():
            prev_is_digit = True
            postfix += char
        elif char == '+' or char == '-':
            if char == '-' and (index == 0 or infix[index - 1] == '('):
                postfix += '0'
            if stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(char)
            prev_is_digit = False
        elif char == '(':
            stack.append(char)
            prev_is_digit = False
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
            prev_is_digit = False

    while stack:
        postfix += stack.pop()

    return postfix


def evaluate_postfix(postfix: list[str]) -> int:
    stack = []
    for char in postfix:
        if char.isdigit() or char[1:].isdigit():
            stack.append(int(char))
        else:
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
            else:
                if char == '+':
                    stack.append(stack.pop() * 1)
                elif char == '-':
                    stack.append(stack.pop() * -1)

    return stack[0]


def calculate(s: str) -> int:
    return evaluate_postfix(infix_to_postfix(s))


if __name__ == '__main__':
    testcases = ["(1+(4+5+2)-3)+(6+8)", "1 + 1", " 2-1 + 2 ", "-(2 + 3)", "-(2 + 7) + (-5)", "2147483647",
                 "1-(     -2)", "1-11", "2-(5-6)"]
    for case in testcases:
        print(f"{case} -> {calculate(case)}")
