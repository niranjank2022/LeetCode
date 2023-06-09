def containsDuplicate(nums: list[int]) -> bool:
    # return len(nums) != len(set(nums))
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)

    return False

def main():
    testcases = [[1, 2, 3, 1], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], [1, 2, 3, 4]]
    for case in testcases:
        print(f"{case} ? {containsDuplicate(case)}")


main()
