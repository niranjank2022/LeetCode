def minCostClimbingStairs(cost: list[int]) -> int:
    cost1: int = 0
    ptr1: int
    cost2: int = 0
    ptr2: int
    for i in range(len(cost) - 2):
        if i == 0:
            cost.append(0)
            ptr1 = i
            cost1 = cost[i]
        if i == 1:
            ptr2 = i
            cost2 = cost[i]
        elif i > 1:
            ptr1 += 1 if cost[ptr1 + 1] <= cost[ptr1 + 2] else 2
            ptr2 += 1 if cost[ptr2 + 1] <= cost[ptr2 + 2] else 2
            cost1 += cost[ptr1]
            cost2 += cost[ptr2]

    cost.pop()
    return cost1 if cost1 < cost2 else cost2


def main():
    testcases = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [0, 0, 1, 1]]
    for case in testcases:
        print(f"{case} -> {minCostClimbingStairs(case)}")


main()
