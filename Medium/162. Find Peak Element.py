def findPeakElement(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    '''
    while low <= high:

        mid = (low + high) // 2
        left = nums[mid - 1] if mid > 0 else - (1 << 31) - 1
        right = nums[mid + 1] if mid + 1 < len(nums) else - (1 << 31) - 1
        if left < nums[mid] and right < nums[mid]:
            return mid
        elif nums[mid] < right:
            low = mid + 1
        else:
            high = mid - 1
    '''
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == '__main__':
    testcases = [[1, 2, 1, 3, 5, 6, 4], [1, 2, 3, 1], [1, 2, 1, 3, 4, 5, 0], [1, 1, 1, 1]]
    for case in testcases:
        print(f"{case} -> {findPeakElement(case)}")
