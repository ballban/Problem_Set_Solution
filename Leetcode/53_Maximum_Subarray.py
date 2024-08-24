class Solution:
    def maxSubArray2(self, nums) -> int:
        sum_value = nums[0]
        max_value = nums[0]
        for num in nums[1:]:
            sum_value += num
            if sum_value > max_value:
                max_value = sum_value

            if sum_value < num:
                sum_value = num

            if num > max_value:
                max_value = num
        return max_value

    def maxSubArray(self, nums) -> int:
        sum_value = 0
        max_value = -10000
        for num in nums:
            sum_value += num
            max_value = max(max_value, sum_value)
            if sum_value < 0:
                sum_value = 0
        return max_value

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))