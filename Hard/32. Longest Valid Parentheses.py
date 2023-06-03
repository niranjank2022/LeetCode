def longestValidParentheses(s: str) -> int:
    if not s:
        return 0

    count = 0
    for i in range(len(s) - 1):

        for j in range(i + 1, len(s)):
            sub_str = ""
            for k in range(i, j + 1):
                sub_str += s[k]
            # print(sub_str, end=' ')
            if isValid(sub_str) and len(sub_str) > count:
                count = len(sub_str)

    return count


def isValid(s: str) -> bool:
    if s == '':
        return False
    stack = [s[0]]
    parentheses = {')': '(', ']': '[', '}': '{'}
    for i in s[1::]:
        if stack and parentheses.get(i) == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return stack == []


if __name__ == '__main__':
    testcases = ["(()", ")()())", "", "()(()"]
    for case in testcases:
        print(f"\'{case}\' -> {longestValidParentheses(case)}")
