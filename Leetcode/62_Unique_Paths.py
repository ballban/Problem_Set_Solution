class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            m, n = n, m

        if m < 2:
            return 1

        dp = [0 for _ in range(m)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, m):
            for j in range(i):
                dp[j] = dp[j] + dp[j - 1]
            dp[i] = dp[i - 1] * 2
            print(dp)
        return dp[n - 1]




s = Solution()
print(s.uniquePaths(24, 24))
