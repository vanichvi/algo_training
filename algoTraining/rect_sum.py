n, m, k = map(int, input().split())
dp = [[0 for x in range(m + 1)] for y in range(n + 1)]
for i in range(1, n + 1):
    nums = input().split()
    for j in range(1, m + 1):
        dp[i][j] = int(nums[j - 1]) + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
# print(dp)
for i in range(k):
    a, b, c, d = map(int, input().split())
    print(dp[c][d] + dp[a - 1][b - 1] - dp[c][b - 1] - dp[a - 1][d])
