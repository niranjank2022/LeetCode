def matrixSumQueries(n: int, queries: list[list[int]]) -> int:
    initial = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    for query in queries:
        answer += query[2] * n

        if query[0] == 0:
            for i in range(n):
                answer -= initial[query[1]][i]
                initial[query[1]][i] = query[2]
        elif query[0] == 1:
            for i in range(n):
                answer -= initial[i][query[1]]
                initial[i][query[1]] = query[2]

    return answer


if __name__ == '__main__':
    testcases = [(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]),
                 (3, [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]])]
    for case in testcases:
        print(f"{case} -> {matrixSumQueries(case[0], case[1])}")
