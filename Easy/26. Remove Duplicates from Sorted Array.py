def removeDuplicates(nums: list[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        while nums[i] == nums[i + 1] and i < len(nums) - 1:
            nums.pop(i)
            nums.append('_')
            i += 1
        else:
            i += 1

    return len(nums)


def main():
    testcases = [[-1, 0, 0, 0, 0], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    print('Hello World')
    for case in testcases:
        print(case)
        print(removeDuplicates(case))


main()
