def topKFrequent(words: list[str], k: int) -> list[str]:
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    Kwords = []
    for word in count:
        Kwords.append((count[word], word))

    Kwords = sorted(Kwords, reverse=True)

    [word[1] for word in Kwords[:k]].sort()
    return


def main():
    testcases = [(["i", "love", "leetcode", "i", "love", "coding"], 2),
                 (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)]
    for case in testcases:
        print(f"{case} --> {topKFrequent(case[0], case[1])}")


main()
