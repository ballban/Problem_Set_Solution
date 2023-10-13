class Solution:
    def numIslands(self, grid) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += _run(i, j, grid)
        return result


def _run(i, j, grid):
    if i < 0 or i >= len(grid):
        return 0
    if j < 0 or j >= len(grid[0]):
        return 0
    if grid[i][j] == "1":
        grid[i][j] = "2"
    else:
        return 0
    _run(i + 1, j, grid)
    _run(i - 1, j, grid)
    _run(i, j + 1, grid)
    _run(i, j - 1, grid)
    return 1


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
s = Solution()
print(s.numIslands(grid))