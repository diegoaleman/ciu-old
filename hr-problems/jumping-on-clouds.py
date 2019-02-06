def jumpingOnClouds(c):
    aux = [0] * len(c)


    for index, cloud in enumerate(c):
        if cloud is not 1:
            jumps = 1000
            if index-1 >= 0 and c[index-1] is not 1:
                jumps = min(aux[index-1] + 1, jumps)
            if index-2 >= 0 and c[index-2] is not 1:
                jumps = min(aux[index-2] + 1, jumps)

            if jumps is not 1000:
                aux[index] = jumps

    print(aux[-1])





arr1 = [0,0,1,0,0,1,0]
arr2 = [0,0,0,0,1,0]
arr3 = [0,1,0,0,0,1,0]
jumpingOnClouds(arr2)
