def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    i, j = 1, 1
    while j < n:
        while j < n and nums[j] == nums[j - 1]:
            j += 1
        if j < n:
            nums[i] = nums[j]
            i += 1
            j += 1

    return i


def main():
    testcases = [[-1, 0, 0, 0, 0], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for case in testcases:
        print(case, end='\t')
        print(removeDuplicates(case))
        print(case)


main()
