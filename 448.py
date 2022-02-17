#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [i for i in range(1, n+1)]
        s = set(s)
        nums = set(nums)
        return list(s.difference(nums))
# @lc code=end

