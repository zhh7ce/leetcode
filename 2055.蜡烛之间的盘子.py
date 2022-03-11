#
# @lc app=leetcode.cn id=2055 lang=python3
#
# [2055] 蜡烛之间的盘子
#

# @lc code=start
from re import M


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        m = len(queries)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            flag = (s[i] == '|')
            dp_temp = 0
            for j in range(i+1, n):
                if s[j] == '*':
                    dp[i][j] = dp[i][j-1]
                    if flag:
                        dp_temp += 1
                else:
                    flag = True
                    dp[i][j] = dp[i][j-1] + dp_temp
                    dp_temp = 0
        res = []
        for x, y in queries:
            res.append(dp[x][y])
        return res
# @lc code=end

