import math

n = int(input())
for _ in range(n):
    r, n = list(int(x) for x in input().split())
    print(int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r))))