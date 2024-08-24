# class Solution:
#     def largestRectangleArea(self, heights) -> int:
#         result = 0
#         # duplicate check list
#         num_list = set()

#         for i in range(len(heights)):
#             if heights[i] in num_list:
#                 num_list = cal_num_list(num_list, heights[i])
#                 continue
#             left = _next(i, -1, heights[i], heights, 1)
#             right = _next(i, 1, heights[i], heights, 1)
#             sum = left + right - heights[i]

#             if sum > result:
#                 result = sum
#             num_list = cal_num_list(num_list, heights[i])

#         return result


# def cal_num_list(num_list, height):
#     if len(num_list) == 0 or height >= max(num_list):
#         num_list.add(height)
#     else:
#         num_list = {x for x in num_list if x <= height}
#     return num_list

# def _next(i, side, height, heights, count):
#     next_num = i + 1 * side

#     # return result when reach the end
#     if next_num < 0 or next_num > len(heights) - 1:
#         return count * height

#     # go next
#     if heights[next_num] >= height:
#         return _next(next_num, side, height, heights, count + 1)
#     else:
#         return count * height

# -------------------------------------------------------------

class Solution:
    def largestRectangleArea(self, heights) -> int:
        # add 0 to end of heights
        heights += [0]
        result = 0
        stack = []
        for i, h in enumerate(heights):
            # if next number is 0, calculate stack and reset
            if h == 0:
                while len(stack) > 0:
                    _s = stack.pop()
                    result = self.get_sum(i, _s[0], _s[1], result)

            # if stack is empty
            # or next number is bigger then last number
            # add index and value to stack
            elif len(stack) == 0 or h > stack[-1][1]:
                stack.append([i, h])

            elif h < stack[-1][1]:
                while len(stack) > 0 and h < stack[-1][1]:
                    _s = stack.pop()
                    result = self.get_sum(i, _s[0], _s[1], result)
                stack.append([_s[0], h])

        return result

    def get_sum(self, i, _i, _h, result):
        sum_value = _h * (i - _i)
        result = sum_value if sum_value > result else result
        return result


# -------------------------------------------------------------

class Solution2:
    def largestRectangleArea(self, heights) -> int:
        # add 0 to end of heights
        heights += [0]
        result = 0
        position = []
        value = []
        for i, h in enumerate(heights):
            # if next number is 0, calculate stack and reset
            if h == 0:
                result = self.cal(result, position, value, i)

            # if stack is empty
            # or next number is bigger then last number
            # add position and value to stack
            elif len(position) == 0 or h > value[-1]:
                position.append(i)
                value.append(h)

            elif h < value[-1]:
                while len(value) > 0 and h < value[-1]:
                    temp_position = position.pop()
                    sum_value = value.pop() * (i - temp_position)
                    if sum_value > result:
                        result = sum_value
                value.append(h)
                position.append(temp_position)
            else:
                pass
        return result

    def cal(self, result, position, value, i):
        while len(position) > 0:
            sum_value = value.pop() * (i - position.pop())
            result = sum_value if sum_value > result else result
        return result


from datetime import datetime

heights = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
heights.append([2, 1, 5, 6, 2, 3])
heights.append([0, 0])
heights.append([1, 1])

# now = datetime.now()
# s = Solution()
# for i in range(100):
#   for height in heights:
#       s.largestRectangleArea(height)
# print(f'time : {datetime.now() - now}')

now = datetime.now()
s2 = Solution2()
for i in range(100):
    for height in heights:
        s2.largestRectangleArea(height)
print(f'time : {datetime.now() - now}')
