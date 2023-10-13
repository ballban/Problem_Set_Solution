# class Solution:
#     def trap(self, height) -> int:
#         # find the first largest number index in heights
#         # separate heights with the number to 2 parts
#         # calculate part 1 and reversed part 2 add them up
#         max_height = max(height)
#         if max_height == 0:
#             return 0
#         index_max = height.index(max_height)
#         result = _trap(height[:index_max] + [max_height])
#         result += _trap(height[index_max:][::-1])
#         return result
#
#
# def _trap(heights):
#     # save the first bar A's index and height
#     # if next bar B is higher than or equal to A
#     # update save point
#     # if B is lower than A then
#     # calculate the water height
#     # which should equal to save_point's height - B's height
#     save_point = [0, heights[0]]
#     water = [0 for _ in range(len(heights))]
#     for i, h in enumerate(heights[1:]):
#         if save_point[1] <= h:
#             save_point = [i, h]
#         else:
#             water[i] = save_point[1] - h
#     return sum(water)

class Solution:
    def trap(self, height) -> int:
        """
        dp
        """
        dp_left = [0 for _ in height]
        dp_right = [0 for _ in height]
        dp_left[0] = height[0]
        dp_right[-1] = height[-1]

        for i in range(1, len(height)):
            dp_left[i] = max(dp_left[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            dp_right[i] = max(dp_right[i + 1], height[i])

        result = 0
        for i in range(len(height)):
            result += min(dp_left[i], dp_right[i]) - height[i]

        return result

height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1] #6
height = [4,3,3,9,3,0,9,2,8,3] #23
s = Solution()
print(height)
print(s.trap(height))