import itertools
from typing import *
import numpy as np
import copy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Doesn't work T_T
        """
        NUMS = range(10)

        np_board = np.array([[int(c) if c != "." else 0 for c in row] for row in board])
        possible_nums_horizontal = [np.setdiff1d(NUMS, row) for row in np_board]
        possible_nums_vertical = [np.setdiff1d(NUMS, col) for col in np_board.T]
        possible_nums_grid = []
        possible_nums_cell = [[[] for y in range(9)] for x in range(9)]

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if i == 9 or j == 9:
                    possible_nums_grid.append(np.setdiff1d(NUMS, np_board[i:, j:].flatten()))
                else:
                    possible_nums_grid.append(np.setdiff1d(NUMS, np_board[i:i + 3, j:j + 3].flatten()))

        while np.sum(np_board) != 405:
            for x in board:
                print("\t".join(x))
            print(np.sum(np_board))
            print("")
            # check each cell with possible_nums_horizontal, vertical, grid
            # if only one number is possible for the cell, then fill it
            for i, j in np.ndindex(np_board.shape):
                if np_board[i, j] != 0:
                    continue

                possible_num_horizontal = possible_nums_horizontal[i]
                possible_num_vertical = possible_nums_vertical[j]
                grid_index = i // 3 * 3 + j // 3
                possible_num_grid = possible_nums_grid[grid_index]

                if len(possible_num_horizontal) == 0:
                    intersect = np.intersect1d(possible_num_grid, possible_num_vertical)
                elif len(possible_num_vertical) == 0:
                    intersect = np.intersect1d(possible_num_grid, possible_num_horizontal)
                elif len(possible_num_grid) == 0:
                    intersect = np.intersect1d(possible_num_horizontal, possible_num_vertical)
                else:
                    intersect = np.intersect1d(np.intersect1d(possible_num_horizontal, possible_num_vertical),
                                               possible_num_grid)

                # print(intersect)
                if len(intersect) == 1:
                    np_board[i, j] = intersect[0]
                    board[i][j] = str(intersect[0])
                    possible_nums_cell[i][j] = []
                    for x in range(i // 3 * 3, i // 3 * 3 + 3):
                        for y in range(j // 3 * 3, j // 3 * 3 + 3):
                            if intersect[0] in possible_nums_cell[x][y]:
                                possible_nums_cell[x][y] = possible_nums_cell[x][y][
                                    possible_nums_cell[x][y] != intersect[0]]
                    possible_nums_horizontal[i] = possible_num_horizontal[possible_num_horizontal != intersect[0]]
                    possible_nums_vertical[j] = possible_num_vertical[possible_num_vertical != intersect[0]]
                    possible_nums_grid[grid_index] = possible_num_grid[possible_num_grid != intersect[0]]
                elif len(intersect) == 0:
                    pass
                else:
                    possible_nums_cell[i][j] = intersect

            # in 3*3 grid, check possible nums in every cell
            # if there is only one cell is possible for one number
            # then fill the cell with that number
            for x in board:
                print("\t".join(x))
            print(np.sum(np_board))
            print("")
            np_possible_nums_cell = np.array(possible_nums_cell)
            for k in range(9):
                i_min, j_min = k // 3 * 3, k % 3 * 3
                i_max, j_max = i_min + 3, j_min + 3
                temp = np_possible_nums_cell[i_min:i_max if i_max != 9 else None,
                       j_min:j_max if j_max != 9 else None].flatten()
                a = []
                for x in temp:
                    if len(x) > 0:
                        a += x.tolist()
                possible_nums = np.setxor1d(a, [], True)
                for num in possible_nums:
                    flag = False
                    num = int(num)
                    for i in range(i_min, i_max):
                        for j in range(j_min, j_max):
                            if num in possible_nums_cell[i][j]:
                                flag = True
                                grid_index = k
                                np_board[i, j] = num
                                board[i][j] = str(num)
                                possible_nums_cell[i][j] = []
                                possible_nums_horizontal[i] = possible_nums_horizontal[i][
                                    possible_nums_horizontal[i] != num]
                                possible_nums_vertical[j] = possible_nums_vertical[j][possible_nums_vertical[j] != num]
                                possible_nums_grid[grid_index] = possible_nums_grid[grid_index][
                                    possible_nums_grid[grid_index] != num]
                                break
                        if flag:
                            break

    def solveSudoku2(self, board: List[List[str]]):
        """
        Recursion
        """
        NUMS = range(10)

        np_board = np.array([[int(c) if c != "." else 0 for c in row] for row in board])
        possible_nums_horizontal = [np.setdiff1d(NUMS, row).tolist() for row in np_board]
        possible_nums_vertical = [np.setdiff1d(NUMS, col).tolist() for col in np_board.T]
        possible_nums_grid = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if i == 9 or j == 9:
                    possible_nums_grid.append(np.setdiff1d(NUMS, np_board[i:, j:].flatten()).tolist())
                else:
                    possible_nums_grid.append(np.setdiff1d(NUMS, np_board[i:i + 3, j:j + 3].flatten()).tolist())

        _recursion(board, 0, 0, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid)

    def solveSudoku3(self, board):
        """
        Recursion without numpy
        """
        nums_horizontal = [set(row) for row in board]
        nums_vertical = [set(col) for col in zip(*board)]
        nums_grid = [set() for x in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    index = i // 3 * 3 + j // 3
                    nums_grid[index].add(board[i][j])

        _recursion2(board, 0, 0, nums_horizontal, nums_vertical, nums_grid)



def _recursion(_board, i, j, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid):
    if i == 9:
        return 1
    if _board[i][j] != ".":
        if j == 8:
            return _recursion(_board, i + 1, 0, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid)
        else:
            return _recursion(_board, i, j + 1, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid)
    else:
        for x in _board:
            print("\t".join(x))
        print("")

        possible_num_horizontal = possible_nums_horizontal[i]
        possible_num_vertical = possible_nums_vertical[j]
        grid_index = i // 3 * 3 + j // 3
        possible_num_grid = possible_nums_grid[grid_index]

        if len(possible_num_horizontal) == 0:
            intersects = np.intersect1d(possible_num_grid, possible_num_vertical)
        elif len(possible_num_vertical) == 0:
            intersects = np.intersect1d(possible_num_grid, possible_num_horizontal)
        elif len(possible_num_grid) == 0:
            intersects = np.intersect1d(possible_num_horizontal, possible_num_vertical)
        else:
            intersects = np.intersect1d(np.intersect1d(possible_num_horizontal, possible_num_vertical),
                                        possible_num_grid)

        if len(intersects) == 0:
            return None

        for intersect in intersects:
            _board[i][j] = str(intersect)
            possible_nums_horizontal[i].remove(intersect)
            possible_nums_vertical[j].remove(intersect)
            possible_nums_grid[grid_index].remove(intersect)
            if j == 8:
                result = _recursion(_board, i + 1, 0, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid)
            else:
                result = _recursion(_board, i, j + 1, possible_nums_horizontal, possible_nums_vertical, possible_nums_grid)

            if result:
                return result
            else:
                _board[i][j] = '.'
                possible_nums_horizontal[i].append(intersect)
                possible_nums_vertical[j].append(intersect)
                possible_nums_grid[grid_index].append(intersect)

        return None


nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
def _recursion2(_board, i, j, nums_horizontal, nums_vertical, nums_grid):
    if i == 9:
        return True
    if _board[i][j] != ".":
        # Continue recursion if number is exist
        # if j == 8 then go next row, else next col
        i, j = (i+1, 0) if j == 8 else (i, j+1)
        return _recursion2(_board, i, j, nums_horizontal, nums_vertical, nums_grid)
    else:
        grid_index = i // 3 * 3 + j // 3
        valid_nums = nums.difference(nums_horizontal[i] | nums_vertical[j] | nums_grid[grid_index])

        if len(valid_nums) == 0:
            return False

        for valid_num in valid_nums:
            _board[i][j] = valid_num
            nums_horizontal[i].add(valid_num)
            nums_vertical[j].add(valid_num)
            nums_grid[grid_index].add(valid_num)

            i_next, j_next = (i + 1, 0) if j == 8 else (i, j + 1)
            if _recursion2(_board, i_next, j_next, nums_horizontal, nums_vertical, nums_grid):
                return True
            else:
                _board[i][j] = '.'
                nums_horizontal[i].remove(valid_num)
                nums_vertical[j].remove(valid_num)
                nums_grid[grid_index].remove(valid_num)

        return False

board_ = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board_ = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", "2", ".", "1", ".", "9", ".", ".", "."],
          [".", ".", "7", ".", ".", ".", "2", "4", "."],
          [".", "6", "4", ".", "1", ".", "5", "9", "."],
          [".", "9", "8", ".", ".", ".", "3", ".", "."],
          [".", ".", ".", "8", ".", "3", ".", "2", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
          [".", ".", ".", "2", "7", "5", "9", ".", "."]]

s = Solution()
s.solveSudoku3(board_)
print("answer:")
for x in board_:
    print("\t".join(x))
# ["5","3","4","6","7","8","9","1","2"],
# ["6","7","2","1","9","5","3","4","8"],
# ["1","9","8","3","4","2","5","6","7"],
# ["8","5","9","7","6","1","4","2","3"],
# ["4","2","6","8","5","3","7","9","1"],
# ["7","1","3","9","2","4","8","5","6"],
# ["9","6","1","5","3","7","2","8","4"],
# ["2","8","7","4","1","9","6","3","5"],
# ["3","4","5","2","8","6","1","7","9"]
