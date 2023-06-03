class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] == 0:
                if not self.dfs(graph, colors, i, 1):
                    return False

        return True

    def dfs(self, graph, colors, node, color):
        if colors[node] != 0:
            return colors[node] == color

        colors[node] = color

        for neighbor in graph[node]:
            if not self.dfs(graph, colors, neighbor, -color):
                return False

        return True


if __name__ == '__main__':
    testcases = [[[1], [0, 3], [3], [1, 2]], [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], [[1, 3], [0, 2], [1, 3], [0, 2]],
                 [[1, 2, 3], [0, 3, 4], [0, 3], [0, 1, 2], [1]]]
    sol = Solution()
    for case in testcases:
        print(f"{case} -> {sol.isBipartite(case)}")
