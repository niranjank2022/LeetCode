from math import isqrt

def bulbSwitch1(n: int):
    bulbs = [True for i in range(n)]

    for i in range(2, n + 1):
        for j in range(i - 1, n, i):
            bulbs[j] = False if bulbs[j] else True

    return bulbs.count(True)


def bulbSwitch2(n: int):
    return isqrt(n)

if __name__ == '__main__':
    testcases = [3, 5, 0, 10, 36]
    for case in testcases:
        print(f"{case} -> {bulbSwitch1(case)}, {bulbSwitch2(case)}")

    num = 12.3


'''
0 0 0 0 0
1 1 1 1 1
1 0 1 0 1
1 0 0 0 1
1 0 0 1 1
1 0 0 1 0
'''