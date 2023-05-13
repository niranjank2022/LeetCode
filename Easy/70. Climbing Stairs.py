def climbStairs(n: int) -> int:
    dp = [1, 1]

    for i in range(1, n + 1):
        step_sum = 0
        if i >= 1:
            step_sum += dp[-1]
        if i >= 2:
            step_sum += dp[-2]
        dp.append(step_sum)
        dp.pop(0)

    return dp[-1]


def main():
    testcases = [2, 3, 10, 11, 4, 25]
    for case in testcases:
        print(f"{case} -> {climbStairs(case)}")


main()
