def circularGameLosers(n: int, k: int) -> list[int]:
    friends = [i for i in range(1, n + 1)]
    curr = 0
    friends[curr] = 0
    for i in range(1, n):
        curr += i * k
        curr %= n
        if friends[curr] == 0:
            break
        friends[curr] = 0

    return [val for val in friends if val != 0]


if __name__ == '__main__':
    testcases = [(5, 2), (4, 4), (1, 1)]
    for case in testcases:
        print(f"{case} -> {circularGameLosers(case[0], case[1])}")
