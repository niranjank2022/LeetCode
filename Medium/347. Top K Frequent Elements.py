import collections
import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequent = {}
    for num in nums:
        frequent[num] = frequent.get(num, 0) + 1

    pairs = sorted(list(frequent.items()), key=lambda x: x[1], reverse=True)
    return [pairs[i][0] for i in range(k)]

    """
    count = collections.Counter(nums)
    heap = [key for key in count]
    print("***", heap)
    heapq.heapify(heap)

    print(heap, "***")
    return [heapq.heappop(heap) for _ in range(k)]
    """


if __name__ == '__main__':
    testcases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([4, 1, -1, 2, -1, 2, 3], 2)]
    for case in testcases:
        print(f"{case} -> {topKFrequent(case[0], case[1])}")
