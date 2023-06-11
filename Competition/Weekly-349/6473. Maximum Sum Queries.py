from collections import defaultdict


def maximumSumQueries(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums1)
    map1, map2 = defaultdict(list), defaultdict(list)

    answer = []
    for x, y in queries:
        value = -1

        if map1[x] or map2[y]:
            for j in map1[x] + map2[x]:
                if nums1[j] >= x:
                    map1[x].append(j)
                if nums2[j] >= y:
                    map2[x].append(j)
                if nums1[j] >= x and nums2[j] >= y:
                    value = max(value, nums1[j] + nums2[j])
        else:
            for j in range(n):
                if nums1[j] >= x:
                    map1[x].append(j)
                if nums2[j] >= y:
                    map2[x].append(j)
                if nums1[j] >= x and nums2[j] >= y:
                    value = max(value, nums1[j] + nums2[j])
                    map2[y].append(j)

        answer.append(value)

    return answer


if __name__ == '__main__':
    testcases = [([2, 1], [2, 3], [[3, 3]]), ([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]),
                 ([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]])]
    for case in testcases:
        print(f"{case} -> {maximumSumQueries(case[0], case[1], case[2])}")
