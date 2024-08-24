import re
class Solution:
    def decodeString1(self, s: str) -> str:
        i = 0
        count_s = 0
        stack = []
        result = ""
        num = ""
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                stack.append([i, 0, num])
                count_s += 1
                num = ""
            elif s[i] == ']':
                j = -1
                while True:
                    if stack[j][1] == 0:
                        stack[j][1] = i
                        break
                    j -= 1
                count_s -= 1
            elif count_s == 0:
                result += s[i]

            if count_s == 0 and len(stack) > 0:
                result += _r(stack, "", s)[0]
            i += 1
        return result


    def decodeString(self, s: str) -> str:
        pattern = "((\d*)\[([^\[\]]*)\])"
        regexs = re.findall(pattern, s)
        while len(regexs) > 0:
            regexs = re.findall(pattern, s)
            for regex in regexs:
                s = s.replace(regex[0], int(regex[1]) * regex[2])
        return s


def _r(stack, text, s):
    start, end, num = stack.pop(0)
    new_text = ""
    if len(stack) > 0:
        new_text, old_text = _r(stack, text, s)
    if new_text:
        text = s[start + 1: end].replace(old_text, new_text)
    else:
        text = s[start + 1: end]
    return text * int(num), s[start - 1: end] + "]"


s = "2[abc]3[cd]ef"
s = "3[a2[c]]"
#s = "3[a]2[bc]"
#s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"

so = Solution()
print(so.decodeString(s))