from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        l = len(nums)
        nums.sort()
        m = nums[-1] - nums[0]
        for i in range(l - 1):
            x = min(nums[0] + k, nums[i + 1] - k)
            y = max(nums[-1] - k, nums[i] + k)
            m = min(m, y - x)
        return m

    def smallestRangeII_2(self, nums: List[int], k: int) -> int:
        arr = sorted(list(set(nums)))
        print(arr)

        res = arr[-1] - arr[0]
        for i in range(len(arr) - 1):
            mx = max(arr[i] + k * 2, arr[-1])
            mn = min(arr[i+1], arr[0] + k * 2)
            print(mx, mn)
            print("mx - mn : ", mx - mn)
            res = min(res, mx - mn)
        return res


nums = [0,10]
k = 2

nums = [1,3,6]
k = 3

nums = [1,6,2,4,8,8]
k = 2

s = Solution()
print(s.smallestRangeII_2(nums, k))