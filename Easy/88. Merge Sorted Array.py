def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = j = 0

    while i < m and j < n:
        if i < m and nums1[i] <= nums2[j]:
            while i < m and nums1[i] <= nums2[j]:
                i += 1
        else:
            nums1.insert(i, nums2[j])
            nums1.pop()
            i += 1
            j += 1
            m += 1

    while j < n:
        nums1.insert(i, nums2[j])
        nums1.pop()
        i += 1
        j += 1


def main():
    testcases = [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), ([1], 1, [], 0), ([0], 0, [1], 1)]
    for case in testcases:
        print(f"{case} ->", end=' ')
        merge(case[0], case[1], case[2], case[3])
        print(case[0])


main()
