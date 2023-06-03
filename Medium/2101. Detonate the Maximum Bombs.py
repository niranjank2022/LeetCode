import collections


def maximumDetonation(bombs: list[list[int]]) -> int:
    answer = 0
    n = len(bombs)
    hashtable = {}
    for i in range(n):
        hashtable[bombs[i][0], bombs[i][1]] = []
        for j in range(n):
            if i != j and ((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2) ** .5 <= bombs[i][2]:
                hashtable[bombs[i][0], bombs[i][1]].append((bombs[j][0], bombs[j][1]))

    # print(hashtable)
    # Doing BFS
    for pt in hashtable:
        freq = hashtable[pt].count(pt)
        visited = {pt}
        queue = collections.deque()
        queue.append(pt)
        while queue:
            for point in hashtable[queue.popleft()]:
                if point not in visited:
                    visited.add(point)
                    queue.append(point)
        answer = max(answer, len(visited) + freq)

    return answer


if __name__ == '__main__':
    testcases = [[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], [[1, 1, 5], [10, 10, 5]],
                 [[2, 1, 3], [6, 1, 4]], [[4, 4, 3], [4, 4, 3]],
                 [[56, 80, 2], [55, 9, 10], [32, 75, 2], [87, 89, 1], [61, 94, 3], [43, 82, 9], [17, 100, 6],
                  [50, 6, 7], [9, 66, 7], [98, 3, 6], [67, 50, 2], [79, 39, 5], [92, 60, 10], [49, 9, 9], [42, 32, 10]]]
    for case in testcases:
        print(f"{case} -> {maximumDetonation(case)}")
