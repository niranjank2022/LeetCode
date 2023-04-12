def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]

    return nums


def main():
    testcases = [[1, 1, 1, 1, 1], [1, 2, 3, 4]]
    for case in testcases:
        print(f"'{case}' ~ {runningSum(case)}")
        print("===============")


main()
