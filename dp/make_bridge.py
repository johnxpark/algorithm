N = 30
dp = [1, 1]
for i in range(2, N + 1):
    dp.append(i * dp[i - 1])

def combination(n, r):
    return int(dp[n] / (dp[r] * dp[n - r]))

n = int(input())
for _ in range(n):
    r, n = list(int(x) for x in input().split())
    print(int(dp[n] / (dp[r] * dp[n - r])))