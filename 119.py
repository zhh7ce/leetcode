#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex-1)
            n = len(prev)
            ans = [1]
            for i in range(1, n):
                ans.append(prev[i] + prev[i-1])
            ans.append(1)
            return ans
# @lc code=end

