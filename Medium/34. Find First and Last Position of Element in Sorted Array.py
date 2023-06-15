def searchRange(nums: list[int], target: int) -> list[int]:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            left = mid - 1
            while left >= 0 and nums[left] == target:
                left -= 1
            right = mid + 1
            while right < len(nums) and nums[right] == target:
                right += 1
            return [left + 1, right - 1]
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return [-1, -1]


if __name__ == '__main__':
    testcases = [([5, 7, 7, 8, 8, 10], 8), ([5, 7, 7, 8, 8, 10], 6), ([], 0)]
    for case in testcases:
        print(f'{case} -> {searchRange(case[0], case[1])}')
