#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(set(nums))
        loss = (n*n + n) // 2 - s
        dup = sum(nums) - s
        return [dup, loss]

# @lc code=end

