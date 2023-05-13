# Contest (Bi-Weekly 104)

def countSeniors(details: list[str]) -> int:
    above_60 = 0
    for data in details:
        age = int(data[11:13])
        if age > 60:
            above_60 += 1

    return above_60