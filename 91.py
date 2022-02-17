#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        array = [1] * (len(s) + 1)
        if s[0] == '0':
            array[0] = 0
            array[-1] = 0
        for i in range(1, len(s)):
            n = int(s[i-1:i+1])
            if n == 0:
                return 0
            elif n < 10:
                array[i] = array[i-1]
            elif n == 10 or n == 20:
                array[i] = array[i-2]
            elif n < 27:
                array[i] = array[i-1] + array[i-2]
            elif s[i] == '0':
                return 0
            else:
                array[i] = array[i-1]
        return array[len(s)-1]
        
# @lc code=end
s = '230'
sol = Solution()
print(sol.numDecodings(s))
