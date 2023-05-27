from typing import Set


def singleNumber(nums: list[int]) -> int:
    """
    hold = 0
    for i in range(len(nums)):
        hold = hold ^ nums[i]

    return hold
    """
    hashSet: set[int] = set()
    for num in nums:
        if num in hashSet:
            hashSet.remove(num)
            continue
        hashSet.add(num)

    return list(hashSet)[0]


if __name__ == '__main__':
    testcases = [[1, 2, 3, 4, 3, 4, 2], [1], [3, 4, 2, 3, 4]]
    for case in testcases:
        print(f"{case} -> {singleNumber(case)}")
