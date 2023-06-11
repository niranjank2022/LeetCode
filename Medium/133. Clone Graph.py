class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    if node is None:
        return None
    if node.neighbors is None:
        return Node(node.val, None)

    hashmap = {}

    def dfs(node: Node):
        if node.val not in hashmap:
            hashmap[node.val] = Node(node.val, [])
            for nd in node.neighbors:
                dfs(nd)
                hashmap[node.val].neighbours.append(hashmap[nd.val])

    dfs(node)
    return hashmap[node.val]
# if __name__ == '__main__':
#     testcases = [["2", "1", "+", "3", "*"], ["4", "13", "5", "/", "+"],
#                  ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
#     for case in testcases:
#         print(f"{case} -> {evalRPN(case)}")
