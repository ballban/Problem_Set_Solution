from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                isSubIsland = self.isSubIsland(grid1, grid2, i, j)
                count += 1 if isSubIsland else 0
        return count

    def isSubIsland(self, grid1, grid2, i, j):
        if i < 0 or j < 0 or i >= len(grid1) or j >= len(grid1[0]):
            return True

        # return if the cell is visited or water
        if grid2[i][j] != 1:
            return False

        # set flag
        subIslandFlag = True
        if grid2[i][j] == 1:
            grid2[i][j] = 2
            if grid1[i][j] == 0:
                subIslandFlag = False

        r1 = self._isSubIsland(grid1, grid2, i, j + 1, subIslandFlag)
        r2 = self._isSubIsland(grid1, grid2, i + 1, j, subIslandFlag)
        r3 = self._isSubIsland(grid1, grid2, i - 1, j, subIslandFlag)
        r4 = self._isSubIsland(grid1, grid2, i, j - 1, subIslandFlag)

        return subIslandFlag and r1 and r2 and r3 and r4

    def _isSubIsland(self, grid1, grid2, i, j, subIslandFlag):
        # return if the cell is out of the grid
        if i < 0 or j < 0 or i >= len(grid1) or j >= len(grid1[0]):
            return True

        # return if the cell is land
        if grid2[i][j] == 1:
            grid2[i][j] = 2
            if grid1[i][j] == 0:
                subIslandFlag = False
        # return if the cell is water
        else:
            return True

        r1 = self._isSubIsland(grid1, grid2, i, j + 1, subIslandFlag)
        r2 = self._isSubIsland(grid1, grid2, i + 1, j, subIslandFlag)
        r3 = self._isSubIsland(grid1, grid2, i - 1, j, subIslandFlag)
        r4 = self._isSubIsland(grid1, grid2, i, j - 1, subIslandFlag)

        return subIslandFlag and r1 and r2 and r3 and r4


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
result = Solution().countSubIslands(grid1, grid2)
print(f"test1: {result == 3}")

grid1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
]
grid2 = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
]
result = Solution().countSubIslands(grid1, grid2)
print(f"test2: {result == 2}")
