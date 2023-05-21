def punishmentNumber(n: int) -> int:
    punish = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 297, 370, 379, 703, 756, 792, 918, 964, 990, 991, 999, 1000]
    sum = 0
    for num in punish:
        if num <= n:
            sum += num ** 2
        else:
            break
    return sum


def punish(num: int) -> bool:
    s = str(num ** 2)
    n = len(s)

    for i in range(1, n):

        length = 1
        while length <= n - i:
            sum = int(s[:i])
            j = i
            while j + length <= n:
                sum += int(s[j:j + length])
                j = j + length
            if s[j:]:
                sum += int(s[j:])
            if sum == num:
                return True
            length += 1

    return False


if __name__ == '__main__':

    for i in range(1, 1001):
        if punish(i):
            print(i, end=' ')
    print()
    print([
        1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379,
        414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000,
    ])
    # for case in [1, 10, 37, 100, 235]:
    #     print(f"{case} -> {punishmentNumber(case)}")
    for i in [235, 369, 414, 657, 675, 909, 945]:
        print(i, i ** 2)

# [235 369, 414, 657, 675, 909, 945]
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 1 2 3 4

# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 5 1 2 3 4 5
