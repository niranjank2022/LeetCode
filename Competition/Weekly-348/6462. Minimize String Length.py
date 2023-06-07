def minimizedStringLength(s: str) -> int:
    return len(set(s))


if __name__ == '__main__':
    testcases = ["aaabc", "cbbd", "dddaaa", "ipi"]
    for case in testcases:
        print(f"{case} -> {minimizedStringLength(case)}")
