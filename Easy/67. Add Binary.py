def addBinary(a: str, b: str) -> str:
    carry = '0'
    binary = ''

    i, j = len(a) - 1, len(b) - 1
    while i >= 0 and j >= 0:
        if a[i] == '1' and b[j] == '1':
            binary = carry + binary
            carry = '1'
        elif a[i] == '1' or b[j] == '1':
            if carry == '1':
                binary = '0' + binary
            else:
                binary = '1' + binary
        else:
            binary = carry + binary
            carry = '0'
        i -= 1
        j -= 1

    while i >= 0:
        if a[i] == '1' and carry == '1':
            binary = '0' + binary
        elif a[i] == '1' or carry == '1':
            binary = '1' + binary
            carry = '0'
        else:
            binary = a[i] + binary
        i -= 1

    while j >= 0:
        if b[j] == '1' and carry == '1':
            binary = '0' + binary
        elif b[j] == '1' or carry == '1':
            binary = '1' + binary
            carry = '0'
        else:
            binary = b[j] + binary
        j -= 1

    if carry == '1':
        binary = carry + binary

    return binary


if __name__ == '__main__':
    testcases = [("11", "1"), ("1010", "1011"), ("11", "11")]
    for case in testcases:
        print(f"{case} -> {addBinary(case[0], case[1])}")
