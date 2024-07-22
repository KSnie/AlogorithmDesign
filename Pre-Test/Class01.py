import sys
sys.setrecursionlimit(10000)

num = list(map(int, input().split()))


def find_number_of_certificates(V):
    certificates = 0
    
    while V > 0:
        a = int(V ** 0.5)
        print(f"V = {V} A = {a * a}")
        V -= a * a

        certificates += 1
        print(certificates)
    
    return certificates

print(find_number_of_certificates(num[0]))