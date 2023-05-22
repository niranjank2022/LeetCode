import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequent = {}
    answer = []
    for num in nums:
        frequent[num] = frequent.get(num, 0) + 1

    pairs = sorted(list(frequent.items()), key=lambda x: x[1], reverse=True)
    for i in range(k):
        answer.append(pairs[i][0])
    return answer


if __name__ == '__main__':
    testcases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1)]
    for case in testcases:
        print(f"{case} -> {topKFrequent(case[0], case[1])}")
