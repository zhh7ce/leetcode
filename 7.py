#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = (x < 0)
        if neg:
            x = -x
        arr = []
        while x > 0:
            arr.append(x % 10)
            x //= 10
        ans = 0
        for i in arr:
            ans *= 10
            ans += i
        if neg:
            if ans > 2147483648:
                return 0
            else:
                return -ans
        else:
            if ans > 2147483647:
                return 0
            else:
                return ans
# @lc code=end

