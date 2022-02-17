#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        n = len(s)
        if n < 4 or n > 12:
            return []
        position = [[0]]
        answer = []
        while position:
            pos = position.pop()
            start = pos[-1]
            left = 4 - len(pos) # left segement
            for length in [1, 2, 3]:
                if n - start - length > 3 * left:
                    continue
                if start + length > n:
                    break
                if not self.isLegal(s[start:start+length]):
                    break
                if left:
                    tmp = pos.copy()
                    tmp.append(start+length)
                    position.append(tmp)
                else:
                    a = ''
                    for i in range(3):
                        a += s[pos[i]:pos[i+1]]
                        a += '.'
                    a += s[pos[3]:]
                    answer.append(a)
        return answer


    def isLegal(self, s:str) -> bool:
        if s != '0' and s[0] == '0':
            return False
        number = int(s)
        if number > 255:
            return False
        return True
# @lc code=end

s = Solution()
print(s.restoreIpAddresses(''))