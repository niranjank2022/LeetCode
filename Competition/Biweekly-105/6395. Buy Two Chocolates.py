def buyChoco(prices: list[int], money: int) -> int:
    prices = sorted(prices)
    if prices[0] + prices[1] <= money:
        return money - (prices[0] + prices[1])
    else:
        return money


if __name__ == '__main__':
    testcases = [([1, 2, 2], 3), ([3, 2, 3], 3)]
    for case in testcases:
        print(f"{case} -> {buyChoco(case[0], case[1])}")
