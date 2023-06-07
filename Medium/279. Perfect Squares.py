import collections


def numSquares(n: int) -> int:
    if n <= 1:
        return n
    queue = collections.deque([n])
    visited = set()
    step = 1
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            for i in range(int(curr ** .5), 0, -1):
                if curr - i ** 2 == 0:
                    return step
                if curr - i ** 2 not in visited:
                    visited.add(curr - i ** 2)
                    queue.append(curr - i ** 2)
        step += 1


if __name__ == '__main__':
    testcases = [12, 13, 0, 1, 2, 26]
    for case in testcases:
        print(f"{case} -> {numSquares(case)}")
