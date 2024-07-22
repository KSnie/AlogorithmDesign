def calHarvesters(gennaration):
    # mother = 0 father = 1
    last_numHarvert = 0
    sum_numberHarvest = 0
    P_gens = []
    N_gen = []

    for i in range(1,gennaration+1):
        numHarvert = 0
        
        if len(P_gens) != 0:
            for i in P_gens:
                if i == 1:
                    N_gen.append(0)
                    N_gen.append(1)
                    numHarvert += 1
                if i == 0:
                    N_gen.append(1)
                    numHarvert += 1

            P_gens = N_gen
            N_gen = []

        if len(P_gens) == 0:
            P_gens.append(1)
        sum_numberHarvest += numHarvert
        last_numHarvert = numHarvert

    Harvesters_count = (sum_numberHarvest-last_numHarvert)+2
    return Harvesters_count

total = calHarvesters(int(input()))
print(f"---------- Total Harvester: {total} --------------")


# chatGpt Version

# def mat_mult(A, B):
#     return [
#         [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
#         [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
#     ]

# def mat_pow(mat, exp):
#     result = [[1, 0], [0, 1]]
#     base = mat

#     while exp:
#         if exp % 2 == 1:
#             result = mat_mult(result, base)
#         base = mat_mult(base, base)
#         exp //= 2

#     return result

# def calHarvesters(generation):
#     if generation == 0:
#         return 1

#     F = [[1, 1], [1, 0]]
#     result = mat_pow(F, generation - 1)

#     Harvesters_count = result[0][0] + result[0][1]
#     return Harvesters_count

# total = calHarvesters(int(input("Enter the generation number: ")))
# print(f"---------- Total Harvester: {total} --------------")
