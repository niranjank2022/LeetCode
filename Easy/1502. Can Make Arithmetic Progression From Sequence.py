def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    n = len(arr)
    d = arr[1] - arr[0]
    for i in range(2, n):
        if d != arr[i] - arr[i - 1]:
            return False

    return True


if __name__ == '__main__':
    testcases = [[3, 5, 1], [1, 2, 4]]
    for case in testcases:
        print(f"{case} -> {canMakeArithmeticProgression(case)}")
