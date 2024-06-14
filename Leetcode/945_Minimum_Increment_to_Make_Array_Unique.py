from typing import List

# Approach 1: Sorting
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        c_min = nums[0]
        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= c_min:
                c_min += 1
                result += c_min - nums[i]
            else:
                c_min = nums[i]
        return result

# Approach 2: Ask chatgpt
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        frequency = [0] * (max(nums) + len(nums))
        for n in nums:
            frequency[n] += 1
        
        taken = 0
        increment = 0

        for i in range(len(frequency)):
            if frequency[i] > 1:
                # count the number of elements that are frequency > 1
                taken += frequency[i] - 1
                # assume all those frequency > 1 elements are at start of the array by drcreasing the distance between them and start of the array 
                increment -= (frequency[i] - 1) * i
            elif taken > 0 and frequency[i] == 0:
                taken -= 1
                # increse the distance between the current elements and the start of the array
                increment += i
        return increment