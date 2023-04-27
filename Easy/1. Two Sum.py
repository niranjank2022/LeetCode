def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def main():
    testcases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6), ([3, 2, 3], 6), ([-1, -2, -3, -4, -5], -8)]
    for case in testcases:
        print(f"{case} -> {twoSum(case[0], case[1])}")


main()
