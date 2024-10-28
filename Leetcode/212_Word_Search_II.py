from typing import List
import time


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make a map for board
        # key is char, values is position
        dic_board = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in dic_board:
                    dic_board[board[i][j]].append((i, j))
                else:
                    dic_board[board[i][j]] = [(i, j)]

        result = []
        for word in words:
            # skip word if char not on board
            if not all(c in dic_board for c in set(word)):
                continue

            # reverse the word if a half of the word from start is same character
            word = word[::-1]

            # start
            for i, j in dic_board[word[0]]:
                used_cell = [[i, j]]
                current_cell = [i, j]
                if len(word) == 1 or self.find_letter(
                    current_cell[0], current_cell[1], board, word, 1, used_cell
                ):
                    result += [word[::-1]]
                    break
        return result

    def find_letter(self, n, m, board, word, letter_index, used_cell):
        # target_cells$ = [[i, j] for i in range(n, n+2, 2) for j in range(m, m+2, 2)]
        target_cells = [[n - 1, m], [n + 1, m], [n, m - 1], [n, m + 1]]
        for target_cell in target_cells:
            result = False
            # if out of index
            if (
                target_cell[0] < 0
                or target_cell[0] >= len(board)
                or target_cell[1] < 0
                or target_cell[1] >= len(board[0])
            ):
                continue

            # if used cell
            if target_cell in used_cell:
                continue

            if board[target_cell[0]][target_cell[1]] == word[letter_index]:
                letter_index += 1
                if letter_index < len(word):
                    used_cell.append([target_cell[0], target_cell[1]])
                    if self.find_letter(
                        target_cell[0],
                        target_cell[1],
                        board,
                        word,
                        letter_index,
                        used_cell,
                    ):
                        return True
                    else:
                        letter_index -= 1
                        used_cell.pop(-1)
                else:
                    return True
        return result


s = Solution()
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]

start_time = time.time_ns()
print(s.findWords(board, words))
print(f"run time: {time.time_ns() - start_time} nanoseconds")

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]

start_time = time.time_ns()
print(s.findWords(board, words))
print(f"run time: {time.time_ns() - start_time} nanoseconds")
