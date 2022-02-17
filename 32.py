#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = 0
        count = [0, 0, 0]
        for i in s:
            if i == '(':
                stack += 1
                count.append(0)
            elif not stack:
                # stack.append(False)
                count.append(-1)
                count.append(0)
            else:
                stack -= 1
                count[-1] += 2
                if count[-2] != -1:
                    count[-2] += count[-1]
                    count[-1] = 0
                    count.pop()
        return max(count)

# @lc code=end

s = "(()(((()"
sol = Solution()
print(sol.longestValidParentheses(s))

