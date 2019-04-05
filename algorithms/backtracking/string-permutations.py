def create_permutations(s):
    permutations(list(s),'')

def permutations(original,result):
    if len(original) == 0:
        print(result)

    for i in range(len(original)):
        concat = original[:]
        del concat[i]
        permutations(concat, result + original[i])


if __name__ == '__main__':
    create_permutations('boat')

