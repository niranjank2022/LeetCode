def finalPrices(prices: list[int]) -> list[int]:
    n = len(prices)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break

    return prices


if __name__ == '__main__':
    testcases = [[8, 4, 6, 2, 3], [1, 2, 3, 4, 5], [10, 1, 1, 6]]
    for case in testcases:
        print(f"{case} -> {finalPrices(case)}")
