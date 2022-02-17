#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        ans = 0
        for i in range(32):
            if mask & n:
                ans += 1
            mask = mask << 1
        return ans
# @lc code=end

