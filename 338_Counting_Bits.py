class Solution:
    # def countBits(self, n: int):
    #     """
    #     90 84%
    #     """
    #     return [bin(x).count('1') for x in range(n + 1)]

    # def countBits(self, n: int):
    #     if len(nums) == 0:
    #         for num in range(100001):
    #             r = 0
    #             while num > 0:
    #                 r += num % 2
    #                 num = num // 2
    #             nums.append(r)
    #     return nums[:n + 1]
# nums = []

    # def countBits(self, n: int):
    #     lit = []
    #     for num in range(n + 1):
    #         n = num
    #         r = 0
    #         while n > 0:
    #             r += n % 2
    #             n = n // 2
    #         lit.append(r)
    #     return lit

    def countBits(self, n: int):
        res = [0] * (n + 1)
        for i in range(1, len(res)):
            if i % 2 != 0:
                res[i] = 1 + res[i - 1]
            else:
                res[i] = res[i // 2]
        return res

n = 1025
s = Solution()
print(s.countBits(n))
lit = []