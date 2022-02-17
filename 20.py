#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif not stack:
                return False
            else:
                j = stack.pop()
                if j == '(' and i == ')':
                    continue
                if j == '{' and i == '}':
                    continue
                if j == '[' and i == ']':
                    continue
                return False
        if stack:
            return False
        return True
# @lc code=end

str = "{{})"
s = Solution()
print(s.isValid(str))
