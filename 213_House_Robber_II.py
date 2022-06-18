from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        return max(rob(nums[:-1]), rob(nums[1:]))


def rob(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    dp = [0, 0] + nums
    for i in range(3, len(nums) + 2):
        dp[i] += max(dp[i - 2], dp[i - 3])
    return max(dp[-1], dp[-2])