class Solution:
    def combinationSum(self, candidates, target: int):
        dp = [[] for _ in range(target + 1)]
        for candidate in candidates:
            if candidate <= target:
                dp[candidate].append([candidate])
        print(dp)

        for i in range(1, len(dp)):
            if dp[i]:
                for j in range(1, i + 1):
                    if dp[j] and i + j < len(dp):
                        for x in dp[i]:
                            a = sorted(dp[j][0] + x)
                            if a not in dp[i + j]:
                                dp[i + j].append(a)
                    print(dp)
        return dp[-1]




can = [2,3,6,7]
t = 7

can = [2,3,5]
t = 8

# can = [1]
# t = 2

s = Solution()
print(s.combinationSum(can, t))
