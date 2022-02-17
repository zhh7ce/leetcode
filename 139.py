#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isTrue = [False] * (len(s) + 1)
        isTrue[0] = True
        maxLength = 0
        for i in wordDict:
            maxLength = max(maxLength, len(i))
        for i in range(len(s)+1):
            for j in range(i, max(-1, i-maxLength), -1):
                if (s[j-1:i] in wordDict) and isTrue[j-1]:
                    isTrue[i] = True
        print(isTrue)
        return isTrue[-1]


# @lc code=end

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print(sol.wordBreak(s, wordDict))