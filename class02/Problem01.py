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
