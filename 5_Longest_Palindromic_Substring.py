# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s
#         result = ''
#         for i, c in enumerate(s):
#             target = len(s)
#             while target != -1 and target - len(result) >= i + 1:
#                 target = s.rfind(c, i + len(result), target)
#                 if target > 0:
#                     check = True
#                     sub = s[i + 1: target]
#                     middle = len(sub) // 2
#                     if len(sub) % 2 == 0:
#                         if sub[:middle] != sub[middle:][::-1]:
#                             check = False
#                     else:
#                         if sub[:middle] != sub[middle + 1:][::-1]:
#                             check = False
#                     if check:
#                         if (target - i + 1) > len(result):
#                             result = s[i: target + 1]

#         if result == '':
#             result = s[0]
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        re_st = 0
        re_ed = 0
        for i in range(len(s)):
            st, ed = self.is_palind(s, i)
            if ed - st + 1 == len(s):
                return s
            if ed - st > re_ed - re_st:
                re_st, re_ed = st, ed

        return s[re_st: re_ed + 1]

    def is_palind(self, str, i):
        st = i
        ed = i

        while ed < len(str) - 1 and str[st] == str[ed + 1]:
            ed += 1

        while st > 0 and ed < len(str) - 1 and str[st - 1] == str[ed + 1]:
            st -= 1
            ed += 1
        return st, ed


# s = "aacabdkacaa"
# s = "abaccab"
# s = "babad"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# s = "ccc"
solution = Solution()
print(solution.longestPalindrome(s))
# "bab"
