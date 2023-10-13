from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i = 0
        j = 0
        result = []
        up = True
        while i < m and j < n:
            result.append(mat[i][j])
            if up:
                if j == n - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                    up = True
                elif j == 0:
                    i += 1
                    up = True
                else:
                    j -= 1
                    i += 1
        return result



#mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2],[3,4]]
#mat = [[1,2,3,4,5,6,7,8,9,10]]

s = Solution()
print(s.findDiagonalOrder(mat))