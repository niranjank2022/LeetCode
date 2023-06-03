def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in strs:
        key = "".join(sorted(word))
        if anagrams.get(key) is None:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)

    return list(anagrams.values())


if __name__ == '__main__':
    testcases = [["eat", "tea", "tan", "ate", "nat", "bat"], [""]]
    for case in testcases:
        print(f"{case} -> {groupAnagrams(case)}")
