def removeStars(s: str) -> str:
    new = list()
    for i in range(len(s)):
        if s[i] == '*':
            new.pop()
            continue
        new.append(s[i])

    return "".join(new)


def main():
    testcases = ["leet**cod*e", "erase*****"]
    for case in testcases:
        print(f"'{case}' - '{removeStars((case))}'")


main()
