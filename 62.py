#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        array = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                array[j] += array[j-1]
        return array[-1]
# @lc code=end

sol = Solution()
print(sol.uniquePaths(7, 3))

