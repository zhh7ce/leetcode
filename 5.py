#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        newS = ['*'] * (2 * len(s) + 1)
        answer = ''
        mid = 0
        length = 0
        for i in range(len(s)):
            newS[2*i + 1] = s[i]
        for i in range(len(newS)):
            maxLength = min(i+1, len(newS)-i)
            for j in range(1, maxLength):
                if newS[i-j] != newS[i+j]:
                    if length < j:
                        length = j-1
                        mid = i
                    break
            else:
                if length < maxLength-1:
                    length = maxLength-1
                    mid = i
        for i in range(mid-length, mid+length+1):
            if newS[i] != '*':
                answer += newS[i]
        print(mid, length)
        return answer
# @lc code=end

sol = Solution()
print(sol.longestPalindrome('vbbd'))

