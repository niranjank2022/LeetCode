def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stack = [n - 1]
    days_to_wait = [0 for _ in range(n)]
    for i in range(n - 2, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()

        days_to_wait[i] = stack[-1] - i if stack else 0
        stack.append(i)

    return days_to_wait


if __name__ == '__main__':
    testcases = [[73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60], [30, 60, 90]]
    for case in testcases:
        print(f"{case} -> {dailyTemperatures(case)}")
