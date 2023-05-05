from collections import deque


def maxVowels(s: str, k: int) -> int:
    stack = deque()
    length = 0
    max_length = 0
    for i in range(len(s)):

        stack.append(s[i])
        if i < k:
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                length += 1
        else:
            if length > max_length:
                max_length = length
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                length += 1
            if stack[0] == 'a' or stack[0] == 'e' or stack[0] == 'i' or stack[0] == 'o' or stack[0] == 'u':
                length -= 1

            stack.popleft()
            if max_length >= k:
                return k

    if length > max_length:
        max_length = length

    return max_length


if __name__ == '__main__':
    testcases = [("abciiidef", 3), ("aeiou", 2), ("leetcode", 3), ("weallloveyou", 7)]
    for case in testcases:
        print(f"{case} -> {maxVowels(case[0], case[1])}")
