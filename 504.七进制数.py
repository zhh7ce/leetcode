#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            res = '-'
            num = -num
        else:
            res = ''

        arr = []
        while num > 0:
            arr.append(str(num % 7))
            num //= 7
        arr.reverse()

        res += ''.join(arr)
        return res
        
# @lc code=end

