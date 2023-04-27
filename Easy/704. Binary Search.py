def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums)
    while high > low:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return -1
