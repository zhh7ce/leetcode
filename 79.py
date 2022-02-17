#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import List
# @lc code=start
import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.length = len(word)
        line = [True] * self.n
        used = []
        for i in range(self.m):
            used.append(line.copy())
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    used[i][j] = False
                    if self.recursion(board, word, used, i, j, 1):
                        return True
                    used[i][j] = True
        return False

    def recursion(self, board, word, used, x, y, index):
        if index >= self.length:
            return True
        for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            if x+i >= 0 and x+i < self.m and \
                y+j >= 0 and y+j < self.n and \
                used[x+i][y+j] and board[x+i][y+j] == word[index]:
                used[x+i][y+j] = False
                if self.recursion(board, word, used, x+i, y+j, index+1):
                    return True
                used[x+i][y+j] = True
        return False


# @lc code=end

board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'ABCCED'
s = Solution()
print(s.exist(board, word))