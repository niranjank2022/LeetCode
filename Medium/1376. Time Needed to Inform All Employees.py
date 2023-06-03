import collections


def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    def dfs(employee: int):
        maxTime = 0
        for subordinate in graph[employee]:
            maxTime = max(maxTime, dfs(subordinate))

        return maxTime + informTime[employee]

    # Forming the graph data
    graph = collections.defaultdict(set)
    for i in range(n):
        if i != headID:
            graph[manager[i]].add(i)

    return dfs(headID)


if __name__ == '__main__':
    testcases = [(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]), (1, 0, [-1], [0]), (
        22, 7, [12, 7, 18, 11, 13, 21, 12, -1, 6, 5, 14, 13, 14, 9, 20, 13, 11, 1, 1, 2, 3, 19],
        [0, 540, 347, 586, 0, 748, 824, 486, 0, 777, 0, 202, 653, 713, 454, 0, 0, 0, 574, 735, 721, 772])]
    for case in testcases:
        print(f"{case} -> {numOfMinutes(case[0], case[1], case[2], case[3])}")
