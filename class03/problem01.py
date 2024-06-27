import sys

# Sample inputs
A = [1,2,5,10,13]
B = [3377]

# val1 = sys.stdin.readline().strip()
# A = list(map(int, val1.split()))

# val2 = sys.stdin.readline().strip()
# B = list(map(int, val2.split()))

def MinimumCoinChange(list, maxval):
    MinimumCount = 9223372036854775807
    CurrentMinimumCount = 0
    for i in list:
        x= sumself(i, maxval)
        CurrentMinimumCount = x[1]
        if (CurrentMinimumCount < MinimumCount):
            if (x[2] == 0):
                MinimumCount = CurrentMinimumCount

            if x[2] in A:
                MinimumCount = x[1] + 1
                print(f"{x[0]} + {x[2]} = {x[0] + x[2]}    Minimumcount = {x[1]} + 1 = {x[1] + 1}")

    print(MinimumCount)


def sumself(num, maxval):
    total = 0
    count = 0
    equal = 0
    while total + num <= maxval:
        total += num
        count += 1
    equal = maxval - total
    return total,count,equal

MinimumCoinChange(A, B[0])
