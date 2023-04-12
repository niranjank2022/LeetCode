def myAtoi(s: str) -> int:
    s = s.strip()
    s = ' ' + s
    s += ' '

    newstr = ""
    for i in range(len(s) - 1):
        if s[i].isalpha():
            return 0
        if s[i].isdigit() or s[i] == '-':
            newstr += s[i]
            if s[i + 1].isalpha():
                break

    return int(newstr)


def main():
    testcases = ["4193 with words", "   -42", "42", "words and 987"]
    for case in testcases:
        print(f"'{case}' ~ {myAtoi(case)}")
        print("===============")


main()
