#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senate = list(senate)
        while True:
            for i in range(n):
                if senate[i] == 'R':
                    x = self.findNext(senate, i, 'D')
                    if x < 0:
                        return 'Radiant'
                    else:
                        senate[x] = 'X'
                elif senate[i] == 'D':
                    x = self.findNext(senate, i, 'R')
                    if x < 0:
                        return 'Dire'
                    else:
                        senate[x] = 'X'
        
    def findNext(self, s, index, c):
        for i in range(index, len(s)):
            if s[i] == c:
                return i
        for i in range(index):
            if s[i] == c:
                return i
        return -1
# @lc code=end

s = Solution()
print(s.predictPartyVictory("DRRDRDRDRDDRDRDR"))