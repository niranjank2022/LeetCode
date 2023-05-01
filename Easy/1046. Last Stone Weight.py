def lastStoneWeight(stones: list[int]):
    while len(stones) >= 2:
        max1 = max(stones)
        stones.remove(max1)
        max2 = max(stones)
        stones.remove(max2)
        if max1 > max2:
            stones.append(max1 - max2)

    return stones[0] if stones else 0


def main():
    testcases = [[2, 7, 4, 1, 8, 1], [1], [5, 3, 8, 8, 9]]
    for case in testcases:
        print(f"{case} -> {lastStoneWeight(case)}")


main()
