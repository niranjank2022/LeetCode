def exists(arr: list[int], start: int, n: int, target: int) -> bool:
    for i in range(start, n):
        if arr[i] == target * 2 or (target % 2 == 0 and arr[i] == target / 2):
            return True

    return False


def checkIfExist(arr: list[int]) -> bool:
    n = len(arr)
    for i in range(n - 1):
        if exists(arr, i + 1, n, arr[i]):
            return True
    return False
