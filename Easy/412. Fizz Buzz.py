def fizzBuzz(n: int) -> list[str]:
    answer = []
    for i in range(1, n + 1):
        char = ""
        if i % 3 != 0 and i % 5 != 0:
            char = str(i)
        else:
            if i % 3 == 0:
                char += 'Fizz'
            if i % 5 == 0:
                char += 'Buzz'
        answer.append(char)

    return answer
