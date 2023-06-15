import collections
import queue


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    map = collections.defaultdict(list)
    for (c1, c2) in prerequisites:
        map[c1].append(c2)

    print(map)
    finished = set()
    for c in map:
        finished.add(c)
        queue = collections.deque(map[c])
        while queue:
            new = queue.popleft()
            if map[new]:
                for i in map[new]:
                    if i in finished:
                        return False
                    finished.add(i)
            else:
                del map[new]
                finished.add(new)


    return True


if __name__ == '__main__':
    testcases = [(2, [[1, 0]]), (2, [[1, 0], [0, 1]]), (3, [[1, 0], [1, 2], [0, 1]]),
                 (10, [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]]), (5, [[1,4],[2,4],[3,1],[3,2]])]
    for case in testcases:
        print(f"{case} -> {canFinish(case[0], case[1])}")
