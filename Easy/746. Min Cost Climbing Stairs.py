def minCostClimbingStairs(cost: list[int]) -> int:
    first_prev = cost[1]
    second_prev = cost[0]
    for val in cost[2:]:
        first_prev, second_prev = min(first_prev, second_prev) + val, first_prev

    return min(first_prev, second_prev)


def main():
    testcases = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [0, 0, 1, 1]]
    for case in testcases:
        print(f"{case} -> {minCostClimbingStairs(case)}")


main()
