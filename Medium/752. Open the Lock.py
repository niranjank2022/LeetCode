import collections


def stepDigit(digit: str, decrement=False) -> str:
    if not decrement:
        return chr(((ord(digit) + 1) % 48 % 10) + 48)
    else:
        if '0' < digit <= '9':
            return chr(ord(digit) - 1)
        elif digit == '0':
            return '9'


def openLock(deadends: list[str], target: str) -> int:
    queue = collections.deque(['0000'])
    visited = set(deadends)
    step = 1
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr in deadends:
                return -1
            if curr == target:
                return step - 1
            for i in range(4):
                for val in (True, False):
                    temp = curr[:i] + stepDigit(curr[i], decrement=val) + curr[i + 1:]
                    if temp == target:
                        return step
                    if temp not in visited:
                        visited.add(temp)
                        queue.append(temp)
        step += 1

    return -1


if __name__ == '__main__':
    testcases = [(["0201", "0101", "0102", "1212", "2002"], "0202"), (["8888"], "0009"),
                 (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"),
                 (["0201", "0101", "0102", "1212", "2002"], "0000"), (["0000"], "9876")]
    for case in testcases:
        print(f"{case} -> {openLock(case[0], case[1])}")
