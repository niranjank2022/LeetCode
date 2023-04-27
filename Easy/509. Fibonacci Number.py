def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    testcases = [1, 2, 3, 4, 5, 6]
    for case in testcases:
        print(f"{case} -> {fib(case)}")


main()
