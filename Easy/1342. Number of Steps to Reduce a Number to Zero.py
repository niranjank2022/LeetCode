def numberOfSteps(num: int) -> int:
    steps = 0
    while num:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps


if __name__ == '__main__':
    testcases = [14, 8, 123, 3]
    for case in testcases:
        print(f"{case} -> {numberOfSteps(case)}")
