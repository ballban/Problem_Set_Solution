from functools import reduce


class Solution:
    # def singleNumber(self, nums) -> int:
    # """
    # 1240~1516 10%
    # """
    #     lit = []
    #     for num in nums:
    #         if num in lit:
    #             lit.remove(num)
    #         else:
    #             lit.append(num)
    #     return lit[0]

    # def singleNumber(self, nums) -> int:
    #     """
    #     666 12%
    #     """
    #     if len(nums) == 1:
    #         return nums[0]
    #     set_nums = set(nums)
    #     for num in set_nums:
    #         nums.remove(num)
    #     result = set_nums - set(nums)
    #     return result.pop()

    # def singleNumber(self, nums) -> int:
    #     """
    #     149 77%
    #     """
    #     dic = {}
    #     for num in nums:
    #         dic[num] = False if num in dic else True
    #
    #     for i in dic:
    #         if dic[i]:
    #             return i

    def singleNumber(self, nums) -> int:
        """
        136~140 90%
        XOR : 0 ^ 5 = 5, 5 ^ 5 = 0
        """
        result = 0
        for num in nums:
            result = result ^ num
        return result
        #return reduce(lambda total, el: total ^ el, nums)


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))

