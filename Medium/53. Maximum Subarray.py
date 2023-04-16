def maxSubArray(nums: list[int]) -> int:
    currSum = 0
    maxSum = nums[0]
    for i in nums:
        currSum += i
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0


    return maxSum


def main():
    testcases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8], [-2, -1]]
    for case in testcases:
        print(f"{case} -> {maxSubArray(case)}")


main()
