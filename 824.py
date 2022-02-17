#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        arr = S.split(' ')
        ans = []
        for index, val in enumerate(arr):
            c = val[0]
            s = ''
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or\
                c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                s += val
                s += 'ma'
                s += 'a' * (index+1)
            else:
                s += val[1:]
                s += c
                s += 'ma'
                s += 'a' * (index+1)
            ans.append(s)
        return ' '.join(ans)
# @lc code=end

