# shity solution by me!
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 1
        n = c
        count = 0
        bool_map = [False] * (c + 1)
        while True:
            count += i
            n -= i
            i += 2
            if n >= 0:
                bool_map[count] = True
            else:
                break

        # print(num_map)

        i = 0
        temp = c
        while temp > 0:
            if bool_map[temp]:
                return True
            i += 1
            temp = c - i ** 2
            # print('temp',temp)
        
        return temp == 0

# chatgpt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        
        while left <= right:
            current_sum = left ** 2 + right ** 2
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        
        return False
