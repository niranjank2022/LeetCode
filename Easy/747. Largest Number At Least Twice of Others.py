def dominantIndex(nums: list[int]) -> int:
    max_element = max(nums)
    max_index = 0
    for i, num in enumerate(nums):
        if num != max_element and num > max_element // 2:
            return -1
        if num == max_element:
            max_index = i

    return max_index