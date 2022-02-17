#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for i in s:
            for j in range(ptr, len(t)):
                if t[j] == i:
                    ptr = j + 1
                    break
            else:
                return False
        return True
# @lc code=end
s = "axc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
