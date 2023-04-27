def singleNumber(nums: list[int]) -> int:
    hold = 0
    for i in range(len(nums)):
        hold = hold ^ nums[i]

    return hold


if __name__ == '__main__':
    testcases = [[1, 2, 3, 4, 3, 4, 2], [1], [3, 4, 2, 3, 4]]
    for case in testcases:
        print(f"{case} -> {singleNumber(case)}")
