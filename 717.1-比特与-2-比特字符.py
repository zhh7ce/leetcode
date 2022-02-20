#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        idx = 0
        while True:
            if bits[idx] == 1:
                idx += 2
                if idx >= n:
                    return False
            else:
                idx += 1
                if idx >= n:
                    return True
# @lc code=end

