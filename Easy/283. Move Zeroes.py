def moveZeroes(nums: list[int]) -> None:
    n = len(nums)
    i = j = 0  # i points to 0 and j points non-zero value's index
    while i < n and j < n:

        while i < n and nums[i] != 0:
            i += 1
        while j < n and nums[j] == 0:
            j += 1

        if i < j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1


if __name__ == '__main__':
    testcases = [[0, 0, 1, 1, 0, 0, 3, 4], [0, 1, 0, 3, 12], [0], [1, 0], [1, 0, 1]]
    for case in testcases:
        print(case, end='\t')
        moveZeroes(case)
        print(case)
