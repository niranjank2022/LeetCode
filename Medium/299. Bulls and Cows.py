def getHint(secret: str, guess: str) -> str:
    letters1 = {}
    letters2 = {}
    cows: int = 0
    bulls: int = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            letters1[secret[i]] = letters1.get(secret[i], 0) + 1
            letters2[guess[i]] = letters2.get(guess[i], 0) + 1

    for k1 in letters1.keys():
        cows += min(letters1.get(k1), letters2.get(k1, 0))

    return f"{bulls}A{cows}B"


def main():
    testcases = [('1807', '7810'), ('1123', '0111'), ('132111', '345671')]
    for case in testcases:
        print(f"Secret: {case[0]} Guess: {case[1]}: {getHint(case[0], case[1])}")


main()
