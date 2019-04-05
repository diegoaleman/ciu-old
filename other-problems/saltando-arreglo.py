# INDEX
# - min que 0
# - max del limite
# - loop (counter < items)
def saltando_arreglo(l):
    index = jumps = 0
    length = len(l)

    while jumps<length:
        if index is length-1:
            return jumps
        if index < 0 or index >= length:
            return -1

        index+=l[index]
        jumps+=1

    return -1

def main():
    N = int(input())
    l = []
    for _ in range(N):
        i = int(input())
        l.append(i)

    print(saltando_arreglo(l))


if __name__ == "__main__":
    main()
