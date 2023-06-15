def findMin(nums: list[int]) -> int:
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]

    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] > nums[low]:
            low = mid + 1
        else:
            high = mid


if __name__ == '__main__':
    testcases = [[3, 4, 5, 1, 2], [4, 5, 6, 7, 0, 1, 2], [11, 13, 15, 17], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                 [4, 5, 1, 2, 3], [5, 1, 2, 3, 4], [9, 8, 9, 9]]
    for case in testcases:
        print(f"{case} -> {findMin(case)}")
