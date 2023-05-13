def validSquare(p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
    points = [p1, p2, p3, p4]
    stack = {}

    for i in range(3):
        for j in range(i + 1, 4):
            if points[i] == points[j]:
                return False
            dist = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** .5
            stack[dist] = stack.get(dist, 0) + 1

    return True if len(stack) == 2 else False


if __name__ == '__main__':
    testcases = [([0, 0], [1, 1], [1, 0], [0, 1]), ([0, 0], [1, 1], [1, 0], [0, 12]),
                 ([1, 0], [-1, 0], [0, 1], [0, -1]), ([0, 0], [1, 1], [0, 0], [0, 0])]

    for case in testcases:
        print(f"{case} -> {validSquare(case[0], case[1], case[2], case[3])}")
