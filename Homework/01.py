# import sys
# sys.setrecursionlimit(10000)

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# V = list(map(int, input().split()))

# x = [0] * N

# def comb(i):
#     if i == N:
#         sw = sv = 0
#         for j in range(N):
#             if x[j] == 1:
#                 sw += W[j]
#                 sv += V[j]
#         if sw > M:
#             return -1
#         else:
#             return sv
#     else:
#         x[i] = 0
#         a = comb(i+1)
#         x[i] = 1
#         b = comb(i+1)
#         return max(a,b)
    
# print(comb(0))


N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

recursion_count = 0
round = 0

def maxVal(i, C):
    global recursion_count
    recursion_count += 1
    global round
    

    if i == N:
        return 0
    else:
        round += 1
        skip = maxVal(i + 1, C)
        print(f"\033[91m[ skip ] = \033[0m{skip}")

        if w[i] <= C:

            print(f"\033[92m[ Value ] = \033[0m W[i] = {w[i]} <= C = {C}")
            take = v[i] + maxVal(i + 1, C - w[i])
            print(f"\033[95m[ TAKE ] = \033[0m{take}")
            # print("++++++++++++++++++++++++++++++++")
            
            
        else:
            take = -1

        print(f"Max In round {round} = {max(skip, take)}")
        print("++++++++++++++++++++++++++++++++")
        return max(skip, take)

result = maxVal(0, M)

print(result)
print("Number of recursive calls:", recursion_count)
