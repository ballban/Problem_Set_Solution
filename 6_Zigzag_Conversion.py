from itertools import cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # row_count start from 1
        # calculate string for each row
        # for row 1
        # result = s[0] + s[down_step] + s[down_step + up_step] + s[down_step + up_step + down_step] ...
        #
        # down_step = 2 * (numRows - row_count)
        # (numRows - row_count) + (numRows - row_count - 1) + 1
        #
        # up_step = 2 * row_count - 2
        # (row_count - 1) + (row_count - 1)

        if numRows == 1 or len(s) < 3:
            return s

        result = ''
        for i in range(numRows):
            down_step = 2 * (numRows - i - 1)
            up_step = 2 * i
            index = i
            flg = True

            # if down_step or up_step <= 0
            # which means the row is first row or last row
            # so take same steps
            down_step = up_step if down_step <= 0 else down_step
            up_step = down_step if up_step <= 0 else up_step

            while index < len(s):
                result += s[index]
                index += down_step if flg else up_step
                flg = not flg
        return result

    def convert2(self, s: str, numRows: int) -> str:

        lines = [""] * numRows

        cycle_range = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        c = cycle(cycle_range)

        for char in s:
            lines[next(c)] += char

        return ''.join(lines)

st = "PAYPALISHIRING"
row = 2
s = Solution()
print(s.convert(st, row))