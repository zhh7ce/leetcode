#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        position = [[0]] 
        # [0, 2, 3] means [0,1], [2] and [3]
        answer = []
        while position:
            pos = position.pop()
            start = pos[-1]
            if start == n:
                tmp = []
                for i in range(len(pos)-1):
                    tmp.append(s[pos[i]:pos[i+1]])
                answer.append(tmp)
                continue
            for end in range(start+1, n+1):
                if self.isPal(s[start:end]):
                    tmp = pos.copy()
                    tmp.append(end)
                    position.append(tmp)
        return answer

    def isPal(self, s:str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
# @lc code=end

s = Solution()
print(s.partition(''))