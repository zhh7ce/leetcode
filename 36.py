#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # line
        for i in board:
            s = set()
            for c in i:
                if c == '.':
                    continue
                if c in s:
                    return False
                else:
                    s.add(c)
        
        # col
        for i in range(9):
            s = set()
            for j in range(9):
                c = board[j][i]
                if c == '.':
                    continue
                if c in s:
                    return False
                else:
                    s.add(c)
        
        # 3 by 3
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                s = set()
                for x in [i, i+1, i+2]:
                    for y in [j, j+1, j+2]:
                        c = board[x][y]
                        if c == '.':
                            continue
                        if c in s:
                            return False
                        else:
                            s.add(c)
        return True
# @lc code=end
matrix = [[".",".",".",".",".",".",".",".","2"],[".",".",".",".",".",".","6",".","."],[".",".","1","4",".",".","8",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".","3",".",".",".","."],["5",".","8","6",".",".",".",".","."],[".","9",".",".",".",".","4",".","."],[".",".",".",".","5",".",".",".","."]]

sol = Solution()
print(sol.isValidSudoku(matrix))

