#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for c in magazine:
            arr[ord(c)-97] += 1
        for c in ransomNote:
            if arr[ord(c)-97]:
                arr[ord(c)-97] -= 1
            else:
                return False
        return True
# @lc code=end

