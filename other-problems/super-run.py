def min_jumps(l):
    index = jumps = 0
    length = len(l)

    while index < length-2:
        if l[index+1] is '#':
            index+=1
        else:
            it = index + 6
            if it > length-1:
                it = length-1
            else:
                while l[it] is ' ':
                    it-=1
            index = it
            jumps+=1

    return jumps


def main():
    l = input()
    print(min_jumps(l))

if __name__ == "__main__":
    main()
