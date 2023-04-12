def pivotIndex(nums: list[int]) -> int:
    S = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        if lsum == S - lsum - nums[i]:
            return i
        lsum += nums[i]
    return -1


def main():
    testcases = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1]]
    for case in testcases:
        print(f"'{case}' ~ {pivotIndex(case)}")
        print("===============")


main()
