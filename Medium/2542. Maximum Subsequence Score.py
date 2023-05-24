from heapq import *


def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    n = len(nums1)
    pairs = [(nums1[i], nums2[i]) for i in range(n)]
    pairs.sort(key=lambda x: x[1], reverse=True)

    heap = []
    heapify(heap)

    heap_sum = 0
    answer = 0
    for i in range(n):

        if i < k - 1:
            heappush(heap, pairs[i][0])
            heap_sum += pairs[i][0]
        else:
            heappush(heap, pairs[i][0])
            heap_sum += pairs[i][0]
            answer = max(answer, heap_sum * pairs[i][1])
            heap_sum -= heappop(heap)

    return answer


if __name__ == '__main__':
    testcases = [([1, 3, 3, 2], [2, 1, 3, 4], 3), ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1)]
    for case in testcases:
        print(f"{case} -> {maxScore(case[0], case[1], case[2])}")
