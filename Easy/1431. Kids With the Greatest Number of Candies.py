def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    mx = max(candies)
    lst = list()
    for i in candies:
        if i + extraCandies >= mx:
            lst.append(True)
        else:
            lst.append(False)

    return lst


def main():
    testcases = [([2, 3, 5, 1, 3], 3), ([4, 2, 1, 1, 2], 1), ([12, 1, 12], 10)]
    for case in testcases:
        print(f"{case} -> {kidsWithCandies(case[0], case[1])}")


main()
