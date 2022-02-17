#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1:
            return s
        n = len(s)
        ans = ''
        distance = (numRows -1) * 2
        index = 0
        while index < n:
            ans += s[index]
            index += distance
        for index in range(1, numRows-1):
            firstStep = distance - index - index
            secondStep = index + index
            first = True
            while index < n:
                ans += s[index]
                if first:
                    index += firstStep
                    first = False
                else:
                    index += secondStep
                    first = True
        index = numRows-1
        while index < n:
            ans += s[index]
            index += distance
        return ans
            
# @lc code=end

