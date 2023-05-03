def countStudents(students: list[int], sandwiches: list[int]) -> int:
    for sndwch in sandwiches:
        n = len(students)
        i = n
        while i > 0 and students[0] != sndwch:
            students.append(students.pop(0))
            i -= 1
        if i <= 0:
            return n
        students.pop(0)

    return 0


if __name__ == '__main__':
    testcases = [([1, 1, 0, 0], [0, 1, 0, 1]), ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])]
    for case in testcases:
        print(f'{case} -> {countStudents(case[0], case[1])}')
