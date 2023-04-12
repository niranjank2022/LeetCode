def isIsomorphic(s: str, t: str) -> bool:
    map = dict()
    for i in range(len(s)):
        if map.get(s[i]) is None and t[i] not in map.values():
            map[s[i]] = t[i]
        elif map.get(s[i]) is None and t[i] in map.values():
            return False
        else:
            if map.get(s[i]) != t[i]:
                return False

    return True


def main():
    testcases = [["egg", "add"], ["foo", "bar"], ["toofan", "loopin"], ["hitler", "killer"]]
    for case in testcases:
        print(f"'{case}' ~ {isIsomorphic(case[0], case[1])}")
        print("===============")


main()
