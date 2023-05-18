def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1]) * sign
    if rev < 1 - (1 << 31) or rev >= 1 << 31:
        return 0
    return rev


if __name__ == '__main__':
    print(1 << 31)
    testcases = [123, 567, -105, 9234542217]
    for case in testcases:
        print(f"{case} -> {reverse(case)}")
