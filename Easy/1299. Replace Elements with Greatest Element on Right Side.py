def replaceElements(arr: list[int]) -> list[int]:
    prev = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > prev:
            arr[i], prev = prev, arr[i]
        else:
            arr[i] = prev

    return arr


if __name__ == '__main__':
    testcases = [[17, 18, 5, 4, 6, 1], [400]]
    for case in testcases:
        print(f"{case} -> {replaceElements(case)}")
