#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = self.maxP(nums)
        nums.reverse()
        p2 = self.maxP(nums)
        return max(p1, p2)
    
    def maxP(self, nums):
        maxNumber = float('-inf')
        maxAbs = 1
        for i in nums:
            if i == 0:
                maxNumber = max(maxNumber, i)
                maxAbs = 1
            else:
                maxNumber = max(maxNumber, maxAbs * i, i)
                maxAbs = maxAbs * i
        return maxNumber

# @lc code=end

n = [2,-5,-2,-4,3]
sol = Solution()
print(sol.maxProduct(n))
