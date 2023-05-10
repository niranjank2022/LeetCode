def infix_to_postfix(s: str) -> list[str]:
    stack = []
    postfix = []
    for indx, char in enumerate(s):

        if char == ' ':
            continue

        elif char.isdigit():
            if postfix and s[indx - 1].isdigit():
                postfix[-1] += char
                continue
            postfix += char

        elif char == '+' or char == '-':
            if not stack:
                stack.append(char)
            else:
                while stack:
                    postfix.append(stack.pop())
                stack.append(char)

        elif char == '*' or char == '/':
            if not stack or stack[-1] == '+' or stack[-1] == '-':
                stack.append(char)
            else:
                postfix.append(stack.pop())
                stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return postfix


def evaluate_postfix(postfix: list[str]) -> int:
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                elif char == '/':
                    stack.append(num1 // num2)

    return stack[0]


def calculate(s: str) -> int:
    return evaluate_postfix(infix_to_postfix(s))


if __name__ == '__main__':
    testcases = ["1+2*5/3+6/4*2", "1*2-3/4+5*6-7*8+9/10", "1-1+1", " 3+5 / 2 ", " 3/2 ", "3+2*2", "1+25/3+6/42"]
    for case in testcases:
        print(f"{case} -> {calculate(case)}")
