def minFlips(a: int, b: int, c: int) -> int:
    n = max(a, b, c).bit_length()

    answer = 0
    for _ in range(n):
        _a, _b, _c = tuple(map(lambda x: bin(x)[-1], (a, b, c)))
        if _c == '1' and (_a == '0' and _b == '0'):
            answer += 1
        if _c == '0':
            if _a == '1' and _b == '1':
                answer += 2
            elif _a == '1' or _b == '1':
                answer += 1
        a, b, c = a >> 1, b >> 1, c >> 1

    return answer


if __name__ == '__main__':
    testcases = [(2, 6, 5), (4, 2, 7), (1, 2, 3)]
    for case in testcases:
        print(f"{case} -> {minFlips(case[0], case[1], case[2])}")
