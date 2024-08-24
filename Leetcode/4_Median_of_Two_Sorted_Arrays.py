from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i_n1 = i_n2 = 0
        nums = []

        total_length = len(nums1) + len(nums2)
        is_even = total_length % 2 == 0
        middle = (len(nums1) + len(nums2)) // 2
        
        while (i_n1 + i_n2) <= middle:
            n1 = nums1[i_n1] if i_n1 < len(nums1) else 1001
            n2 = nums2[i_n2] if i_n2 < len(nums2) else 1001
            if n1 < n2:
                nums.append(n1)
                i_n1 += 1
            elif n1 > n2:
                nums.append(n2)
                i_n2 += 1
            else:
                nums.append(n1)
                i_n1 += 1

                if (i_n1 + i_n2) <= middle:
                    nums.append(n2)
                    i_n2 += 1

        if is_even and total_length > 1:
            return (nums[-1] + nums[-2]) / 2
        else:
            return nums[-1]
    
s = Solution()
print(s.findMedianSortedArrays([2,2,4,4], [2,2,4,4]))