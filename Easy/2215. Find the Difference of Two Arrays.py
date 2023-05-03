def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)

    return [list(nums1 - nums2), list(nums2 - nums1)]


if __name__ == '__main__':
    testcases = [([1, 2, 3], [2, 4, 6]), ([1, 2, 3, 3], [1, 1, 2, 2])]
    for case in testcases:
        print(f"{case} -> {findDifference(case[0], case[1])}")
