from typing import List

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
                taken += frequency[i] - 1
                increment -= (frequency[i] - 1) * i
            elif taken > 0 and frequency[i] == 0:
                taken -= 1
                increment += i
        return increment