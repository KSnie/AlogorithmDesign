# ‘k’ kilograms apples
# ‘n’ friends

_countTestCases = int(input())
answer = []

for i in range(_countTestCases):
    N, K = map(int, input().split())
    packets = list(map(int, input().split()))
    avaliable_packets = []
    avaliable_price = []

    for i in range(0, len(packets)):
        if (packets[i] == -1):
            continue
        
        kilo_packets = i + 1
        price = packets[i]
        avaliable_packets.append(kilo_packets)
        avaliable_price.append(price)

    minPrice = []

    for i in avaliable_packets:
        _count = K - i
        if _count in avaliable_packets:
            minPrice.append(avaliable_price[avaliable_packets.index(i)] + avaliable_price[avaliable_packets.index(_count)])

    if len(minPrice) == 0:
        answer.append(-1)
    else:
        answer.append(min(minPrice))

for i in answer:
    print(i)