def nextGreatestLetter(letters: list[str], target: str) -> str:
    low, high = 0, len(letters) - 1
    while low < high:
        mid = (low + high) // 2
        if letters[mid] > target:
            high = mid
        else:
            low = mid + 1

    return letters[low] if letters[low] > target else letters[0]
