def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    answer = []
    for i in range(n - 1):
        target = -nums[i]
        j, k = i + 1, n - 1
        while j < k:
            if nums[j] + nums[k] == target:
                answer.append([nums[i], nums[j], nums[k]])
            j, k = j + 1, k - 1

    return answer
    """answer: list[list[int]] = []
    nums = sorted(nums)
    for i in range(len(nums)):
        target = -nums[i]
        j = i + 1
        k = len(nums) - 1
        while k > j:
            if nums[j] + nums[k] == target:
                if not (nums[i - 1] == nums[i] or nums[j - 1] == nums[j] or nums[k + 1] == nums[k]):
                    answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] < target:
                j += 1

    return answer
    
    """


def main():
    testcases = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0, 0]]
    for case in testcases:
        print(f"{sorted(case)} -> {threeSum(case)}")
        # print(sorted(case))


main()
