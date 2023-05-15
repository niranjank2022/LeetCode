def removeElement(nums: list[int], val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(val)

    return len(nums)


if __name__ == '__main__':
    testcases = [([0, 1, 2, 2, 3, 0, 4, 2], 2), ([3, 2, 2, 3], 3)]
    for case in testcases:
        print(f"{case} -> {removeElement(case[0], case[1])} {case[0]}")
