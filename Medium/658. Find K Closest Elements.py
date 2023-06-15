def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    if arr[0] > x:
        return arr[:k]
    if arr[-1] < x:
        return arr[len(arr) - k:]

    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid + 1] - x > x - arr[mid]:
            right = mid
        else:
            left = mid

    if k == 1:
        return [arr[left]] if abs(x - arr[left]) <= abs(x - arr[right]) else [arr[right]]

    while right - left + 1 < k:
        if left == 0:
            return arr[:k]
        elif right == len(arr):
            return arr[-k:]
        else:
            if x - arr[left - 1] <= arr[right + 1] - x:
                left -= 1
            else:
                right += 1

    return arr[left:right + 1]


'''
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    if x < arr[0]:
        return arr[:k]
    if x > arr[-1]:
        return arr[len(arr) - k:]

    low, high = 0, len(arr) - 1
    left, right = 0, 0
    while low < high:
        mid = (low + high) // 2
        left, right = mid, mid + 1
        if arr[mid] <= x <= arr[mid + 1]:
            break
        elif arr[mid] <= x:
            low = mid + 1
        else:
            high = mid

    if arr[left] > x or arr[right] < x:
        left = right

    if k == 1:
        return [arr[left]]
    diff = max(x - arr[left], arr[right] - x)
    while right - left + 1 < k:
        while left - 1 >= 0 and x - arr[left - 1] <= diff and right - left + 1 < k:
            left -= 1
        while right + 1 < len(arr) and arr[right + 1] - x <= diff and right - left + 1 < k:
            right += 1
        diff += 1

    return arr[left: right + 1]
'''

if __name__ == '__main__':
    testcases = [([1, 2, 3, 4, 5], 4, -1), ([1, 2, 3, 4, 5], 4, 3), ([7], 1, -2), ([1, 1, 1, 10], 1, 9),
                 ([1, 2, 3, 4, 4, 4, 4, 5, 5], 3, 3), ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5)]
    for case in testcases:
        print(f"{case} -> {findClosestElements(case[0], case[1], case[2])}")
