#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs[0])
        for i in strs:
            n = min(n, len(i))
        for i in range(n):
            if not self.isSame(strs, i):
                return strs[0][:i]
        else:
            return strs[0][:n]

    def isSame(self, strs, i):
        c = strs[0][i]
        for j in strs:
            if j[i] != c:
                return False
        return True
# @lc code=end

