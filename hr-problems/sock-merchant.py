from collections import Counter

def sockMerchant(n, ar):
    ocurrences = Counter(ar)
    pairs = list(ocurrences.items())
    counter = 0

    for key,val in pairs:
        counter += (val // 2)

    return counter
