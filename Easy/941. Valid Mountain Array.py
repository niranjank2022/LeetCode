def validMountainArray(arr: list[int]) -> bool:
    n = len(arr)
    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1
    if i == n - 1 or i == 0:
        return False
    for i in range(i, n - 1):
        if arr[i + 1] >= arr[i]:
            return False

    return True


if __name__ == '__main__':
    testcases = [[2, 1], [3, 5, 5], [0, 3, 2, 1], [0, 2, 3, 4, 5, 2, 1, 0]]
    for case in testcases:
        print(f"{case} -> {validMountainArray(case)}")
