def minOperations(logs: list[str]) -> int:
    depth = 0
    for operation in logs:
        if '../' in operation:
            if depth > 0:
                depth -= 1
        elif './' in operation:
            continue
        elif '/' in operation:
            depth += 1

    return depth


if __name__ == '__main__':
    testcases = [["d1/", "d2/", "../", "d21/", "./"], ["d1/", "d2/", "./", "d3/", "../", "d31/"],
                 ["d1/", "../", "../", "../"]]
    for case in testcases:
        print(f"{case} -> {minOperations(case)}")
