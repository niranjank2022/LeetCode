def firstUniqChar(s: str) -> int:
    hashmap = {}
    for i, v in enumerate(s):
        if hashmap.get(v) is None:
            hashmap[v] = 1, i
        else:
            hashmap[v] = hashmap[v][0] + 1, i

    for key in hashmap:
        if hashmap[key][0] == 1:
            return hashmap[key][1]
    return -1


"""
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
"""

if __name__ == '__main__':
    testcases = ["leetcode", "loveleetcode", "aabb", "aadadaad"]

    for case in testcases:
        print(f"{case} -> {firstUniqChar(case)}")
