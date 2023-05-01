def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    greater = []
    for i in range(len(nums1)):
        j = lSearch(nums2, nums1[i])
        if j != -1:
            for num in nums2[j:]:
                j = -1
                if num > nums1[i]:
                    j = num
                    break
        greater.append(j)

    return greater


def lSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == '__main__':
    testcases = [([4, 1, 2], [1, 3, 4, 2]), ([2, 4], [1, 2, 3, 4]), ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7])
                 ]
    # for case in testcases:
    #     # print(case[0], case[1])
    #     print(f"{case} -> \n{nextGreaterElement(case[0], case[1])}")

    print(nextGreaterElement(testcases[2][0], testcases[2][1]))
