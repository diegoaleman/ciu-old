def repeatedString(s, n):
    count_a = s.count('a')
    length = len(s)

    div = n // length
    rem = n % length

    result = count_a * div
    if rem > 0:
        result += s[:rem].count('a')

    return result

