def print_triangle(N):
    brick = 1
    space = N//2

    while brick <= N:
        print(' '*space, end='')
        print('@'*brick, end='')
        print(' '*space)
        # print('{}{}{}'.format(' '*space, '@'*brick, ' '*space))
        brick+=2
        space-=1


def main():
    N = int(input())
    print_triangle(N)

if __name__ == "__main__":
    main()
