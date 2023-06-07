def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    sieve = [1 for i in range(2, n)]
    i = 2
    hFactor = int(n ** .5)
    while i <= hFactor:
        while sieve[i - 2] == 0:
            i += 1
        for j in range(i * 2, n, i):
            sieve[j - 2] = 0
        i += 1

    return sieve.count(1)


if __name__ == '__main__':
    testcases = [10, 0, 1, 50]
    for case in testcases:
        print(f"{case} -> {countPrimes(case)}")
