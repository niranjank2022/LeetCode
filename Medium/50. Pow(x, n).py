'''
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    return myPow(x, n - 1) * x
'''


def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1 or x == 1 or x == 0:
        return x
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2 == 0:
        return myPow(x * x, n // 2)
    else:
        return x * myPow(x, n - 1)


if __name__ == '__main__':
    testcases = [(2.0, -2), (2.1, 3), (2, 10), (2, 2), (0.00001, 2147483647)]
    for case in testcases:
        print(f"{case} -> {myPow(case[0], case[1])}")
