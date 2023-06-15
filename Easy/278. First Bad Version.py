def isBadVersion(version: int) -> bool:
    return True or False


def firstBadVersion(n: int) -> int:
    low = 1
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


"""
def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
"""
