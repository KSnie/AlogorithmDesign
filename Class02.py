import sys
sys.setrecursionlimit(10000) # set recursion-stack depth

# def generating_combinations(n):
#     count = n
#     max = pow(2, n-1)
#     max_comb = (max*2)-1

#     print(f"combinations has {max_comb+1}")
    
#     def comb(i):
#         if (i <= max_comb):
#             num = format(i, f"0{count}b")
#             res = list(map(int, str(num)))
#             print(res)
#             comb(i+1)
#         else:
#             return
#     comb(0)

# generating_combinations(4)



import sys
sys.setrecursionlimit(10000)

x = []

def generating_combinations(n):
    global x
    x = [0] * n

    def comb(i):
        if i == n:
            print(x)
            return 1
        else:
            count = 0
            for val in [0, 1]:
                x[i] = val
                count += comb(i + 1)
            return count

    total_combinations = comb(0)
    print(f"Total combinations: {total_combinations}")

generating_combinations(100)
