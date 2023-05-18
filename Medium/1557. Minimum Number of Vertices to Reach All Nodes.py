def findSmallestSetOfVertices(n: int, edges: list[list[int]]) -> list[int]:
    _from, _to = set(), set()
    for edge in edges:
        _from.add(edge[0])
        _to.add(edge[1])

    return list(_from - _to)


if __name__ == '__main__':
    testcases = [(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]), (5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]])]
    for case in testcases:
        print(f"{case} -> {findSmallestSetOfVertices(case[0], case[1])}")
