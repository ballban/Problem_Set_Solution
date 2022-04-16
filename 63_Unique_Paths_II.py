class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        return _re(0, 0, obstacleGrid, 0)

def _re(i, j, grid, result):
    m, n = len(grid), len(grid[0])
    com_i = i < m - 1
    com_j = j < n - 1
    if not com_i and not com_j:
        return result + 1
    else:
        if com_j and grid[i][j + 1] == 0:
            result = _re(i, j + 1, grid, result)
        if com_i and grid[i + 1][j] == 0:
            result = _re(i + 1, j, grid, result)
        if (com_i and com_j and grid[i][j + 1] == 1 and grid[i + 1][j] == 1)\
                or (not com_i and grid[i][j + 1] == 1)\
                or (not com_j and grid[i + 1][j] == 1):
            grid[i][j] = 1
    return result


from typing import List
from collections import defaultdict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return unique_paths_with_obstacle(obstacleGrid)


def unique_paths_with_obstacle(grid: List[List[int]]):
    gx = len(grid)
    gy = len(grid[0])
    dp = defaultdict(int)
    for i in range(gx):
        for j in range(gy):
            if grid[i][j] == 1:
                dp[(i, j)] = 0
            elif i == 0 & j == 0:
                dp[(i, j)] = 1
            else:
                x = dp[(i - 1, j)]
                y = dp[(i, j - 1)]
                dp[(i, j)] = x + y
    return dp[(gx - 1, gy - 1)]

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid = [[0,1],[0,0]]
grid = [[1]]
grid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
for row in grid:
    x = [" " if _ == 0 else "1" for _ in row]
    print("\t".join(x))
s = Solution()
print(s.uniquePathsWithObstacles(grid))
