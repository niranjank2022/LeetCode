import collections


def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if not stack:
                return False
            stack.pop()

    return stack == []


def removeInvalidParentheses(s: str) -> list[str]:
    if isValid(s):
        return [s]
    unique = []
    visited = set()
    queue = collections.deque([s])

    # Doing BFS
    dist = 1
    short = 1 << 31
    while queue:
        for _ in range(len(queue)):
            if dist > short:
                return unique
            string = queue.popleft()
            for i in range(len(string)):
                if not string[i].islower():

                    sub_string = string[:i] + string[i + 1:]
                    if sub_string in visited:
                        continue
                    visited.add(sub_string)
                    if isValid(sub_string):
                        if dist <= short:
                            unique.append(sub_string)
                            short = dist
                    else:
                        queue.append(sub_string)

        dist += 1

    if not unique:
        return [s]
    return unique


if __name__ == '__main__':
    testcases = ["()())()", "(a)())()", ")(", "n", "a(b)c", "(y", "((()((s((((()"]
    for case in testcases:
        print(f"{case} -> {removeInvalidParentheses(case)}")
