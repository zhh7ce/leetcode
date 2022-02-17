#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        s = s[::-1]
        for i in s:
            if i == ' ':
                if count == 0:
                    continue
                else:
                    return count
            count += 1
        return count
# @lc code=end

