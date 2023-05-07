def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target and (mid == end or nums[mid + 1] > target):
            return mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


def lengthOfLIS(nums: list[int]) -> int:
    lis = []
    length = 0
    for num in nums:
        if not lis:
            lis.append(num)
            length += 1
        else:
            indx = binary_search(lis, num)
            if indx >= length:
                lis.append(num)
                length += 1
            else:
                lis[indx] = num

    return length


if __name__ == '__main__':
    testcases = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7, 7, 7, 7, 7]]
    for case in testcases:
        print(f"{case} -> {lengthOfLIS(case)}")
