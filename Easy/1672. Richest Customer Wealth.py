def maximumWealth(accounts: list[list[int]]) -> int:
    return max([sum(customer) for customer in accounts])


if __name__ == '__main__':
    testcases = [[[1, 2, 3], [3, 2, 1]], [[1, 5], [7, 3], [3, 5]], [[2, 8, 7], [7, 1, 3], [1, 9, 5]]]
    for case in testcases:
        print(f"{case} -> {maximumWealth(case)}")
