from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 1
        i = 0
        j = 1
        while i < len(nums) - 1:
            while j < len(nums):
                if self.isNice(nums[i : j + 1]):
                    result = max(result, j - i + 1)
                    j += 1
                else:
                    j = i + 2 if j - i == 1 else j
                    break
            i += 1
        return result

    def isNice(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] & nums[-1] > 0:
                return False
        return True


array = [
    744437702,
    379056602,
    145555074,
    392756761,
    560864007,
    934981918,
    113312475,
    1090,
    16384,
    33,
    217313281,
    117883195,
    978927664,
]
s = Solution()
print(s.longestNiceSubarray(array))
print(s.longestNiceSubarray2(array))
