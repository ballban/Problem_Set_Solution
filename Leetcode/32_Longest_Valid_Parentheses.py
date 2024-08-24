# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         result = 0
#         # record start index
#         stack = []
#         # flag
#         flag = True
#         count = 0
#         temp = 0
#         for i, c in enumerate(s):
#             if c == '(':
#                 if len(stack) == 0:
#                     temp += count
#                     count = 0
#                 stack.append(i)
#             else: # c == ')'
#                 if len(stack) == 0:
#                     #flag = False
#                     count += temp
#                     result = count if count > result else result
#                     count = 0
#                     temp = 0
#                     continue

#                 last = stack.pop()

#                 current = i - last + 1

#                 # if flag:
#                 if current > count:
#                     count = current
#                 else:
#                     count += current
#                 # else:
#                 #     count = current
#                 #     flag = True

#         count += temp
#         result = count if count > result else result
#         return result


# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         nums = [0 if c == '(' else 1 for c in s]
#         result = 0
#         # record start index, end index, end - start
#         stack = []
#         for i, num in enumerate(nums):
#             if num == 0:
#                 stack.append([i, i, 0])
#             else: # num == 1
#                 if len(stack) == 0:
#                     continue

#                 # find valid ( in stack
#                 j = -1
#                 while stack[j][2] != 0:
#                     j -= 1
#                     if j*-1 > len(stack):
#                         result = _cal(stack, result)
#                         break

#                 if len(stack) == 0:
#                     continue

#                 if j < -1:
#                     del stack[j + 1:]

#                 # update end index
#                 stack[-1][1] = i
#                 stack[-1][2] = stack[-1][1] - stack[-1][0]

#                 while 1==1:
#                     if len(stack) > 1 and stack[-2][2] != 0 and stack[-2][1] + 1 == stack[-1][0]:
#                         stack[-2][1] = stack[-1][1]
#                         stack[-2][2] = stack[-2][1] - stack[-2][0]
#                         stack.pop()
#                     else:
#                         break

#         result = _cal(stack, result)
#         return result

# def _cal(stack, result):
#     while len(stack) > 0:
#         k = stack.pop()
#         if k[2] == 0:
#             continue
#         count = k[2] + 1
#         result = count if count > result else result
#     return result

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         result = 0
#         result_list = _cal(s, 0, [])
#         i=0
#         while 1==1:
#             if result_list[i][2] == 0:
#                 continue

#         return result


# def _result(l, i, count, result):
#     if i == len(l):
#         return result
#     if l[i][2] == 0:
#         return _result(l, i+1, result)


#     count += l[i][2] + 1


# def _cal(s, i, result):
#     if len(s) == i:
#         return result

#     if s[i] == "(":
#         # record start index, end index, end-start value
#         result.append([i,i,0])
#         return _cal(s, i + 1, result)
#     else: # )
#         # if result is empty then go next
#         if len(result) == 0:
#             return _cal(s, i + 1, result)

#         # get last valid ( and update end index
#         j = -1
#         while result[j][2] != 0:
#             j -= 1
#             if j*-1 > len(result):
#                 return _cal(s, i + 1, result)
#         result[j][1] = i
#         result[j][2] = i - result[j][0]
#         return _cal(s, i + 1, result)


# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) < 2:
#             return 0

#         # delete ( at beginning of the string
#         i = 0
#         while i < len(s) and s[i] != '(':
#             i += 1
#         if i == len(s):
#             return 0
#         else:
#             s = s[i:]

#         # delete ) at end of the string
#         j = len(s) - 1
#         while j > 0 and s[j] != ')':
#             j -= 1
#         if j == 0:
#             return 0
#         elif j != len(s) - 1:
#             s = s[:j + 1]

#         left_count = s.count('(')
#         right_count = len(s) - left_count
#         if left_count > right_count:
#             s = _reverseString(s)

#         result = _cal([], 0, s, 0, 0)
#         return result

# def _cal(stack, i, s, result, count):
#     if i == len(s):
#         result = count if count > result else result
#         return result

#     if s[i] == '(':
#         stack.append('(')
#         return _cal(stack, i + 1, s, result, count)
#     else: #s[i] == ')'
#         if len(stack) == 0:
#             result = count if count > result else result
#             s = s[i + 1:]
#             s = _reverseString(s)
#             return _cal([], 0, s, result, 0)
#         else:
#             stack.pop()
#             return _cal(stack, i + 1, s, result, count + 2)
# def _reverseString(s):
#     s = ['(' if c == ')' else ')' for c in s]
#     s = s[::-1]
#     return s

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0 for x in s]
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # c == ')'
                if len(stack) == 0:
                    pass
                else:
                    left_index = stack.pop()
                    if left_index == 0:
                        dp[left_index] = i + 1
                    else:
                        dp[left_index] = dp[left_index - 1] + i - left_index + 1
                    dp[i] = dp[left_index]
            # print(dp)

        return max(dp)

    def a(self, s: str) -> int:
        if len(s) < 2:
            return 0
        max_num = 0
        temp_max = 0
        stack = ''
        for c in s:
            if c == '(':
                stack += c
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    temp_max += 2
                    stack = stack[:-1]
                    if len(stack) == 0:
                        max_num = temp_max if temp_max > max_num else max_num
                        temp_max = 0
                elif temp_max > 0:
                    max_num = temp_max if temp_max > max_num else max_num
                    temp_max = 0
        return max(max_num, temp_max)
                    

s = ["("]  # 0
s += ["()"]  # 2
s += ["(()"]  # 2
s += ["()(()"]  # 2
s += ["())()"]  # 2
s += ["(()())"]  # 6
s += ["()(())()(())"]  # 12
s += ["(()(()()))()()()()))"]  # 18
s += ["(()(())))()(())()())))"]  # 10
s += ["()(()((())("]  # 4
s += ["))("]  # 0
s += ["))))))))"]  # 0
s += ["(((((((("]  # 0
s += ["))))())()()(()"]  # 4
s += ["((()()(()((()"]  # 4

so = Solution()
for k in s:
    print(so.a(k))

