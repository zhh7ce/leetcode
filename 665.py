#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if changed:
                    return False
                else:
                    changed = True
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
# @lc code=end

