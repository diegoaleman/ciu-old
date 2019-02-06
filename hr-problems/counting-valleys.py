def countingValleys(n, s):
    trail, counter = 0, 0
    valley = False

    conversion = {'U':1, 'D':-1}

    for item in s:
        trail += conversion[item]

        if not valley and trail < 0:
            valley = True

        if valley and trail == 0:
            valley = False
            counter += 1

    return counter

arr = ['U','D','D','D','U','D','U','U']

print(countingValleys(8,arr))
