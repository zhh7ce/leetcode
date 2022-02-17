#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        n = len(s)
        prev = set()
        for i in range(n):
            if s[i] in prev:
                continue
            else:
                prev.add(s[i])
                if s[i] not in s[i+1:]:
                    return i
        return -1
# @lc code=end

