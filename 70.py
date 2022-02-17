#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        array = [1] * (n + 1)
        array[1] = 2
        for i in range(2, n):
            array[i] = array[i-1] + array[i-2]
        return array[n-1]
# @lc code=end
sol = Solution()
print(sol.climbStairs(1))
