def minExtraChar(s: str, dictionary: list[str]) -> int:
    dictionary.sort(key=lambda x: len(x), reverse=True)
    for word in dictionary:
        posi = s.find(word)
        if posi == -1:
            allowed = True
            for letter in word:
                if letter not in s:
                    allowed = False
                    break

            if allowed and len(word) < len(s):
                dictionary.append(word)
                dictionary.pop(0)
                # dictionary.pop(0)
            # print(word, s, dictionary)
            continue
        s = s[:posi] + s[posi + len(word):]
        # print(s)
        # dictionary.remove(word)

    # print(dictionary)
    return len(s)


if __name__ == '__main__':
    testcases = [("dwmodizxvvbosxxw",
                  ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo", "cehy", "tskz", "ds",
                   "kzbu"]), ("leetscode", ["leet", "code", "leetcode"]), ("sayhelloworld", ["hello", "world"])]
    for case in testcases:
        print(f"{case} -> {minExtraChar(case[0], case[1])}")
