def findDisappearedNumbers(nums: list[int]) -> list[int]:
    n = len(nums)
    nums.sort()
    answer = []
    # Numbers between 1 and the minimum element in the array that were disappeared
    val = 1
    while val < nums[0]:
        answer.append(val)
        val += 1
    i = 1

    # Numbers between the minimum and maximum that were disappeared
    while i < n:
        if nums[i] - nums[i - 1] > 1:
            val = nums[i - 1] + 1
            while val < nums[i]:
                answer.append(val)
                val += 1
        i += 1

    # Numbers between the maximum and n that were disappeared
    val = nums[-1] + 1
    while val <= n:
        answer.append(val)
        val += 1

    return answer


if __name__ == '__main__':
    testcases = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1]]
    for case in testcases:
        print(f"{case} -> {findDisappearedNumbers(case)}")
