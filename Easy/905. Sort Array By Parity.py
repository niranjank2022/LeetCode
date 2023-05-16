def sortArrayByParity(nums: list[int]) -> list[int]:
    n = len(nums)
    i = j = 0  # i points odd int and j points even int
    while i < n and j < n:
        while i < n and nums[i] % 2 == 0:
            i += 1
        while j < n and nums[j] % 2 != 0:
            j += 1

        if i < j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return nums


if __name__ == '__main__':
    testcases = [[3, 1, 2, 4], [1, 10, 3, 12], [0], [1, 10], [1, 2, 1]]
    for case in testcases:
        print(case, end='\t')
        sortArrayByParity(case)
        print(case)
