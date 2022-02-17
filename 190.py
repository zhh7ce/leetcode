#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        tmp = 2147483648
        for i in range(32):
            if n & 1:
                ans += tmp
            tmp >>= 1
            n >>= 1
        return ans
# @lc code=end

