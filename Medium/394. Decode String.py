from collections import deque


def decodeString(s: str) -> str:
    count = deque()
    letters = deque()
    token = str()
    currstr = str()
    isToken: bool
    for letter in s:

        if letter.isdigit():
            count.append(int(letter))


        elif letter == '[':

            isToken = True
            letters.append(token)
            token = ''


        elif letter.isalpha():
            if isToken:
                token += letter
            else:
                letters.append(letter)


        elif letter == ']':
            isToken = False

            if token:
                letters.append(token)
                # token = token * count.pop()

            currstr = (letters.pop() + currstr) * count.pop()
            token = ''

    return currstr


def main():
    testcases = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for case in testcases:
        print(f"{case} -> {decodeString(case)}")

    # print(decodeString(testcases[1]))


main()
