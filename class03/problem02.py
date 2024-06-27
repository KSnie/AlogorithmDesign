import sys

# val1 = sys.stdin.readline().strip()
# prices = list(map(int, val1.split()))

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

call_count = 0

def rod_cutting(prices, l):
    global call_count
    call_count += 1
    if l == 0:
        return 0
    max_revenue = float('-inf')
    for i in range(1, l + 1):
        max_revenue = max(max_revenue, prices[i - 1] + rod_cutting(prices, l - i))
    return max_revenue

for length in range(1, 11):
    call_count = 0
    max_revenue = rod_cutting(prices, length)
    print(f"Length: {length}, Max Revenue: {max_revenue}, Function Calls: {call_count}")
