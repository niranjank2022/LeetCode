def removeDuplicates(nums: list[int]) -> int:
    i = len(nums) - 1
    while i > 0:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        i -= 1


def main():
    testcases = [[-1, 0, 0, 0, 0], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for case in testcases:
        print(case, end='\t')
        removeDuplicates(case)
        print(case)


main()
