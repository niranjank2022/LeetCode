def removeElement(nums: list[int], val: int) -> int:
    n = len(nums)
    i = j = 0
    while i < n and j < n:
        while i < n and nums[i] != val:
            i += 1
        while j < n and nums[j] == val:
            j += 1

        if i < j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return i


if __name__ == '__main__':
    testcases = [([0, 1, 2, 2, 3, 0, 4, 2], 2), ([3, 2, 2, 3], 3)]
    for case in testcases:
        print(case, end='\t')
        removeElement(case[0], case[1])
        print(case[0])
