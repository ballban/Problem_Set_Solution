from typing import *


class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) < 2:
#             return True
#         return _recursion(nums, len(nums) - 2, len(nums) - 1)
#
#
# def _recursion(nums, i, i_base):
#     if i_base - i > nums[i]:
#         if i == 0:
#             return False
#         else:
#             return _recursion(nums, i - 1, i_base)
#     else:
#         if i == 0:
#             return True
#         else:
#             i_base = i
#             return _recursion(nums, i_base - 1, i_base)

    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums)):
            # if we can get directly to the end from the current index, then
            # we've found a valid solution
            if i == len(nums) - 1:
                return True

            # if the current list value permits us to take even more steps
            # than the previous maximum list value observed, then increase
            # the number of remaining possible steps
            if step < nums[i]:
                step = nums[i]

            # if step reaches 0 and we're not already at the end (which is
            # already checked by the first if statement), there's no way for
            # us to reach the end
            if step == 0:
                return False

            # if we didn't get a True or False result out of the current step
            # value, decrement and try the next one
            step = step - 1




nums = [[2, 3, 1, 1, 4]]
nums.append([3, 2, 1, 0, 4])
nums.append([1,0])
nums.append([5, 2, 1, 0, 1, 5])
nums.append([0])
nums.append([1])
nums.append([1,2,3])
nums.append([[1,1,2,2,0,1,1]])
s = Solution()
for num in nums:
    print(s.canJump(num))