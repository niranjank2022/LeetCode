import collections


def equalPairs(grid: list[list[int]]) -> int:
    n = len(grid)
    count = 0
    if n == 1:
        return 1

    hashmap = collections.defaultdict(int)
    for i in range(n):
        hashmap[tuple(grid[i])] += 1

    for i in range(n):
        count += hashmap.get(tuple([grid[j][i] for j in range(n)]), 0)

    return count


if __name__ == '__main__':
    testcases = [[[3, 2, 1], [1, 7, 6], [2, 7, 7]], [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], [[19]]]
    for case in testcases:
        print(f"{case} -> {equalPairs(case)}")
