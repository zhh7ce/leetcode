#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and self.illegal(stack[-1], i):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
    
    def illegal(self, x, y):
        if x == y:
            return False
        if x.lower() == y or x.upper() == y:
            return True
        return False
# @lc code=end

