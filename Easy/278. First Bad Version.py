def isBadVersion(version: int) -> bool:
    ...


def firstBadVersion(n: int) -> int:
    low = 0
    high = n - 1
    while high >= low:
        mid = (low + high) // 2
        if isBadVersion(mid + 1):
            if not isBadVersion(mid):
                return mid + 1
            else:
                high = mid - 1
        else:
            low = mid + 1


firstBadVersion(5)
