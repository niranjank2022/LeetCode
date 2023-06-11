import collections


def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    unlocked = {0}
    queue = collections.deque([0])

    while queue:
        for i in rooms[queue.popleft()]:
            if i not in unlocked:
                unlocked.add(i)
                queue.append(i)

    return len(unlocked) == len(rooms)


if __name__ == '__main__':
    testcases = [[[1], [2], [3], []], [[1, 3], [3, 0, 1], [2], [0]]]
    for case in testcases:
        print(f"{case} -> {canVisitAllRooms(case)}")
