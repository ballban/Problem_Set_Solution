class Solution:
    def combinationSum3(self, k: int, n: int):
        """
        ゴミ
        """
        result = []

        # find min sum and check n
        min_n = sum(range(k))
        if n < min_n:
            return []

        # find max sum and check n
        max_n = sum(range(10 - k, 10))
        if n > max_n:
            return []

        # make a list from 1 to k - 1
        # and last number should be n - sum of previous nums
        # ex. [1, 2, 3, 15]
        dp = [x for x in range(1, k)]
        dp.append(n - sum(range(k)))
        print(dp)

        # if the last number is bigger than 9
        # adjust previous number let last number equal to 9
        x = dp[-1] - 9
        i = -1
        while x > 0:
            dp[i] = 10 + i
            dp[i - 1] += x
            i -= 1
            x = dp[i] - (10 + i)
        print(dp)

        i = 0
        while k > 3:
            count = 0
            while count < k:
                if len(set(dp)) == k:
                    x = sorted(dp)
                    if x not in result:
                        result.append(x)

                if dp[0] < dp[1] - 1:
                    dp[0] += 1
                    dp[1] -= 1
                    count = 0
                elif k > 2 and dp[1] < dp[2] - 1:
                    dp[1] += dp[0]
                    dp[0] = 1
                    dp[2] -= 1
                    count = 0
                else:
                    count += 1

                if i == k - 1:
                    i = 0
                print(dp)
            return result




k = 3
n = 15

k = 2
n = 6

k = 4
n = 24

s = Solution()
print("result", s.combinationSum3(k, n))