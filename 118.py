#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            line = [1]
            prev = ans[-1]
            for i in range(len(prev)-1):
                line.append(prev[i] + prev[i+1])
            line.append(1)
            ans.append(line)
        return ans
# @lc code=end

