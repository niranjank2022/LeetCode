def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    dp = [1]
    actual_sum = 0
    M = 10 ** 9 + 7
    for i in range(1, high + 1):
        good_sum = 0
        if i >= zero:
            good_sum += dp[i - zero]
        if i >= one:
            good_sum += dp[i - one]

        dp.append(good_sum % M)
        if low <= i <= high:
            actual_sum += dp[i]

    return actual_sum


if __name__ == '__main__':
    testcases = [[3, 3, 1, 1], [2, 3, 1, 2], (200, 200, 10, 1)]
    for case in testcases:
        print(f"{case} -> {countGoodStrings(case[0], case[1], case[2], case[3])}")
