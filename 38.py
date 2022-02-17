#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        strs = self.countAndSay(n-1)
        ans = ''
        point = -1
        n = len(strs)
        for i in range(n-1):
            if strs[i] != strs[i+1]:
                ans += str(i - point)
                ans += strs[i]
                point = i
        ans += str(n-1 - point)
        ans += strs[n-1]
        return ans

# @lc code=end

