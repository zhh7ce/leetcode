#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float('-inf')
        n = float('-inf')
        for i in nums:
            m = max(m+i, i)
            n = max(n, m)
            # print(m, n)
        return n
# @lc code=end
n =[-2,1,-3,4,-1,-1,-1,6]
sol = Solution()
print(sol.maxSubArray(n))

