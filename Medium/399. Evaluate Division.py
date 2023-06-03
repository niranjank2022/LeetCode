from collections import defaultdict


def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    graph = defaultdict(dict)

    for (u, v), val in zip(equations, values):
        graph[u][u] = graph[v][v] = 1
        graph[u][v] = val
        graph[v][u] = 1 / val

    for k in graph:
        for i in graph[k]:
            for j in graph[k]:
                graph[i][j] = graph[i][k] * graph[k][j]

    return [graph[u].get(v, -1) for u, v in queries]


"""def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    n = len(equations)
    results = {}
    answers = []

    if n < 2:
        results[equations[0][0]], results[equations[0][1]] = {}, {}
        results[equations[0][0]][equations[0][1]] = values[0]
        results[equations[0][1]][equations[0][0]] = 1 / values[0]

    else:
        for i in range(n - 1):
            if results.get(equations[i][0]) is None:
                results[equations[i][0]] = {}
            if results.get(equations[i][1]) is None:
                results[equations[i][1]] = {}
            results[equations[i][0]][equations[i][1]] = values[i]
            results[equations[i][1]][equations[i][0]] = 1 / values[i]

            for j in range(i + 1, n):
                if results.get(equations[j][0]) is None:
                    results[equations[j][0]] = {}
                if results.get(equations[j][1]) is None:
                    results[equations[j][1]] = {}

                results[equations[j][0]][equations[j][1]] = values[j]
                results[equations[j][1]][equations[j][0]] = 1 / values[j]
                if equations[i][1] == equations[j][0]:
                    results[equations[i][0]][equations[j][1]] = values[i] * values[j]
                    results[equations[j][1]][equations[i][0]] = 1 / (values[i] * values[j])

                if equations[i][1] == equations[j][1]:
                    results[equations[i][0]][equations[j][0]] = values[i] / values[j]
                    results[equations[j][0]][equations[i][0]] = values[j] / values[i]
    print(results)
    for query in queries:
        if results.get(query[0]):
            if results[query[0]].get(query[1]):
                answers.append(results[query[0]][query[1]])
                continue
            elif query[0] == query[1]:
                answers.append(1.0)
                continue

        answers.append(-1.0)

    return answers"""

if __name__ == '__main__':
    testcases = [([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]], [3.0, 4.0, 5.0, 6.0],
                  [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]),
                 (
                     [["a", "b"], ["b", "c"]], [2.0, 3.0],
                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]), (
                     [["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                     [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
                 ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]), ([["a", "e"], ["b", "e"]]
                                                                                           , [4.0, 3.0],
                                                                                           [["a", "b"], ["e", "e"],
                                                                                            ["x", "x"]])]

    for case in testcases:
        print(f" -> \n{calcEquation(case[0], case[1], case[2])}")
