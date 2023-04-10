def longestCommonPrefix(strs: list[str]) -> str:
    prefix = list(strs[0])
    for index in range(1, len(strs)):

        if (len(strs[index]) > len(prefix)):  # Increasing the size to match the size of string to compare with
            for i in range(len(strs[index]) - len(prefix)):
                prefix.append(' ')

        newPrefix = list()
        for i, v in enumerate(strs[index]):  # Finding the common prefix
            if v != prefix[i]:
                break
            newPrefix.append(v)

        prefix = newPrefix
        if prefix == []:
            return ""

    return "".join(prefix)


def main():
    testcases = [["dog", "racecar", "car"], ["flower", "flow", "flight"]]
    for case in testcases:
        print(case, "==>", longestCommonPrefix(case))


main()
