def firstUniqChar(s: str) -> int:
    unique = {}
    letters = {}
    for key, val in enumerate(s):
        if letters.get(val) is None:
            unique[val] = key
        else:
            if unique.get(val) is not None:
                del unique[val]
        letters[val] = key

    if len(unique) >= 1:
        return list(sorted(unique.values()))[0]
    return -1


if __name__ == '__main__':
    testcases = ["leetcode", "loveleetcode", "aabb", "aadadaad"]

    for case in testcases:
        print(f"{case} -> {firstUniqChar(case)}")
