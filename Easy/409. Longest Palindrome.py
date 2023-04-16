def longestPalindrome(s: str) -> int:
    letters = dict()
    oddIsPresent: bool = False
    count = 0
    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    for n in letters.values():
        if n % 2 == 0:
            count += n
        else:
            oddIsPresent = True
            count += n - 1

    if oddIsPresent:
        count += 1
    return count


def main():
    testcases = ["abccccdd", "a", "aA", "malayalams"]
    for case in testcases:
        print(f"{case} -> {longestPalindrome(case)}")


main()
