import collections


def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    hashmap = collections.defaultdict(int)

    for n1 in nums1:
        for n2 in nums2:
            hashmap[-(n1 + n2)] += 1

    count = 0
    for n1 in nums3:
        for n2 in nums4:
            count += hashmap[n1 + n2]

    return count


if __name__ == '__main__':
    testcases = [[[-1, -1], [-1, 1], [-1, 1], [1, -1]], [[1, 2], [-2, -1], [-1, 2], [0, 2]]]
    for case in testcases:
        print(f"{case} -> {fourSumCount(case[0], case[1], case[2], case[3])}")
