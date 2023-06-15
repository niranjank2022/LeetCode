import collections


def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:
    buses = collections.defaultdict(list)
    for bus in range(len(routes)):
        for stop in routes[bus]:
            buses[stop].append(bus)


    print("\n", buses, "\n")
    visited = {source}
    buses_travelled = set()
    targetReached = False

    def traverse(start):
        bus_count = 0
        nonlocal targetReached
        for bus in buses[start]:
            if bus not in buses_travelled:
                bus_count += 1
                buses_travelled.add(bus)
                for stop in routes[bus]:
                    if stop not in visited:
                        visited.add(stop)
                        if stop == target:
                            targetReached = True
                            return bus_count
                        bus_count += traverse(stop)

        return bus_count if targetReached else 0

    answer = traverse(source)
    return answer if answer != 0 else -1


if __name__ == '__main__':
    testcases = [([[1, 2, 7], [3, 6, 7]], 1, 6), ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12),
                 ([[1, 2, 7], [3, 6, 7]], 1, 6), (
                 [[1, 9, 12, 20, 23, 24, 35, 38], [10, 21, 24, 31, 32, 34, 37, 38, 43], [10, 19, 28, 37], [8], [14, 19],
                  [11, 17, 23, 31, 41, 43, 44], [21, 26, 29, 33], [5, 11, 33, 41], [4, 5, 8, 9, 24, 44]], 37, 28)]
    for case in testcases:
        print(f"{case} -> {numBusesToDestination(case[0], case[1], case[2])}")
