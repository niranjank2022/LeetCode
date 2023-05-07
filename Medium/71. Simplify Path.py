def simplifyPath(path: str) -> str:
    lst = path.split('/')
    stack = ['/']
    for char in lst:

        if char == '':
            continue
        if len(stack) > 1 and char == '..':
            stack.pop()
            stack.pop()
        elif char != '' and char != '.' and char != '..':
            stack.append(char)
            stack.append('/')
    if len(stack) > 1:
        stack.pop()
        return "".join(stack)
    else:
        return "/"


if __name__ == '__main__':
    testcases = ["/home/", "/../", "/home//foo/", "/a/./b/./c/./d/", "/a/../.././../../.", "/a/./b/../../c/"]
    for case in testcases:
        print(f"{case} -> {simplifyPath(case)}")
