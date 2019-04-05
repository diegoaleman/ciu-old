def LRS(l):
    screening = set()
    result = []

    for letter in l:
        if letter in screening:
            result.append(letter)
        else:
            screening.add(letter)
    return''.join(result)

if __name__ == '__main__':
    l = "AGGVGBTABEBCDD"
    print(LRS(list(l)))

