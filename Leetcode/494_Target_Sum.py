from typing import *


class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """
        Trying to solve it with not recursive way
        """
        zero_count = len([0 for x in nums if x == 0])
        non_zero = [x for x in nums if x != 0]

        result = 0
        memo = {}
        NON_ZERO_MAX_INDEX = len(non_zero) - 1
        deepth = NON_ZERO_MAX_INDEX
        total = sum(non_zero)

        while deepth < 0:
            if (deepth, total) in memo:
                # result += memo[(deepth, total)]
                pass
            else:
                total -= non_zero[deepth]
                for i in range(deepth, NON_ZERO_MAX_INDEX):
                    total = total + non_zero[i]
                    if (i, total) in memo:
                        pass
                    else:
                        if i == NON_ZERO_MAX_INDEX:
                            memo[(deepth, total)] = 1 if total == target else 0

                    total = total - non_zero[i]
                    if (i, total) in memo:
                        pass
                    else:
                        if i == NON_ZERO_MAX_INDEX:
                            memo[(deepth, total)] = 1 if total == target else 0
                deepth -= 1

        result = result * 2 ** zero_count
        return result

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        Bitwise operation(Not recursive)
        Easy to understand, but slow
        """
        zero_count = len([0 for x in nums if x == 0])
        non_zero = [x for x in nums if x != 0]
        shift_list = [1 << x for x in range(len(non_zero))]

        result = 0
        cases = 2 ** len(non_zero)
        for i in range(cases):
            total = 0
            for j in range(len(non_zero)):
                if (i & shift_list[j]) != 0:
                    total += non_zero[j]
                else:
                    total -= non_zero[j]
            if total == target:
                result += 1

        result = result * 2 ** zero_count
        return result

    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        """
        Recursive way
        """

        def dp(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            postive = dp(i + 1, sum + nums[i])
            negative = dp(i + 1, sum - nums[i])
            return postive + negative

        return dp(0, 0)

    def findTargetSumWays4(self, nums: List[int], target: int) -> int:
        """
        Recursive way with memoization
        """
        memo = {}

        def dp(i, sum):
            if (i, sum) in memo:
                return memo[(i, sum)]
            if i == len(nums):
                if sum == target:
                    memo[(i, sum)] = 1
                else:
                    memo[(i, sum)] = 0
                return memo[(i, sum)]
            postive = dp(i + 1, sum + nums[i])
            negative = dp(i + 1, sum - nums[i])
            memo[(i, sum)] = postive + negative
            return memo[(i, sum)]

        return dp(0, 0)

    def findTargetSumWays5(self, nums: List[int], target: int) -> int:
        """
        Recursive way with memoization(ver 2)
        """
        zero_count = len([0 for x in nums if x == 0])
        non_zero = [x for x in nums if x != 0]

        memo = {}

        def dp(i, sum):
            if (i, sum) in memo:
                return memo[(i, sum)]
            if i == len(non_zero):
                if sum == target:
                    memo[(i, sum)] = 1
                else:
                    memo[(i, sum)] = 0
                return memo[(i, sum)]
            postive = dp(i + 1, sum + non_zero[i])
            negative = dp(i + 1, sum - non_zero[i])
            memo[(i, sum)] = postive + negative
            return memo[(i, sum)]

        return dp(0, 0) * 2 ** zero_count

    def findTargetSumWays6(self, nums, S):
        """
        Solution from internet
        """
        self.ways = 0
        cache = {}

        def rec_build(i, currsum):
            # add] in index and current sum to cache
            if (i, currsum) not in cache:
                # update our cache when we have use all elements
                if i == len(nums):
                    # a]solution of elements with valid sum
                    if currsum == S:
                        cache[(i, currsum)] = 1
                    # not] valid sum
                    else:
                        cache[(i, currsum)] = 0
                # if] we we have not used all the elements keep recursing and adding to cache
                else:
                    cache[(i, currsum)] = rec_build(
                        i + 1, currsum + nums[i]) + rec_build(
                        i + 1, currsum - nums[i])
            return cache[(i, currsum)]

        return rec_build(0, 0)

    def findTargetSumWays7(self, nums: List[int], target: int) -> int:
        """
        wtf is this?
        """
        diff = sum(nums) - target
        if diff % 2 or abs(sum(nums)) < abs(target):
            return 0

        goal_sum_n = abs(diff // 2)

        dp = [1] + [0] * (goal_sum_n)
        # 1,0,0,0,0,0,0,0,0,0,0,0,0....

        for num in nums:
            for j in range(goal_sum_n, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[-1]

    def findTargetSumWays8(self, nums: List[int], target: int) -> int:
        # [1,2,3,4]
        sum_t = sum(nums)  # 10
        # sum_p = sum of positives
        # sum_n = sum of nagatives

        # sum_t = sum_p + sum_n
        # sum_p - sum_n == target # 2
        # sum_p = target + sum_t - sum_p
        # sum_p = (sum_t + target) / 2

        if sum_t < target:
            return 0
        if (sum_t + target) % 2:
            return 0

        sum_p_max = (sum_t + target) // 2  # 6

        # init
        dp = [[1] + [0] * sum_p_max]
        for num in nums:
            dp.append([0] * (sum_p_max + 1))
        i = 0
        for num in nums:
            for goal in range(sum_p_max + 1):
                if goal >= num:
                    dp[i + 1][goal] = dp[i][goal] + dp[i][goal - num]
                else:
                    dp[i + 1][goal] = dp[i][goal]
            i += 1
        print(dp)
        return dp[-1][-1]


from datetime import datetime

# nums = [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47]
# target = 38
# 1  : 0:00:18.338715
# 2  : 0:00:09.493225
# 3  : 0:00:08.615102

# nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
# target = 35
# 1  : 0:00:37.754539
# 2  : 0:00:20.505429

# nums = [
#     2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12,
#     38
# ]
# target = 48
# 1  : 0:00:38.651378
# 2  : 0:00:18.621938
# 3  : 0:00:20.775091

# nums = [27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0]
# target = 10
# 2  : 0:00:09.187328
# 3  : 0:00:10.807808

# nums = [1, 2, 3, 4]
# target = 2

# s1 = Solution()
# start_time = datetime.now()
# print(f"result: {s1.findTargetSumWays1(nums, target)}")
# print(f"time  : {datetime.now()-start_time}")

# s2 = Solution()
# start_time = datetime.now()
# print(f"result: {s2.findTargetSumWays2(nums, target)}")
# print(f"time  : {datetime.now()-start_time}")

# s3 = Solution()
# start_time = datetime.now()
# print(f"result3: {s3.findTargetSumWays4(nums, target)}")
# print(f"time   : {datetime.now()-start_time}")

# s4 = Solution()
# start_time = datetime.now()
# print(f"result4: {s4.findTargetSumWays5(nums, target)}")
# print(f"time   : {datetime.now()-start_time}")

# s7 = Solution()
# start_time = datetime.now()
# print(f"result7: {s7.findTargetSumWays7(nums, target)}")
# print(f"time   : {datetime.now()-start_time}")

# s8 = Solution()
# start_time = datetime.now()
# print(f"result8: {s8.findTargetSumWays8(nums, target)}")
# print(f"time   : {datetime.now()-start_time}")

nums = [27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0]
test = [x for x in nums if x > 30]
