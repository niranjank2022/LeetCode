def maxProfit(prices: list[int]) -> int:
    cheapever = prices[0]
    profit = 0
    for i in prices[1::]:
        if i < cheapever:
            cheapever = i
        if i - cheapever > profit:
            profit = i - cheapever
    return profit


def main():
    testcases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    for case in testcases:
        print(f"{case} -> {maxProfit(case)}")


main()
