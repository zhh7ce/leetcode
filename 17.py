#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dictory = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        array = ['']
        for i in digits:
            tmp = []
            for j in array:
                for k in dictory[int(i)-2]:
                    tmp.append(j + k)
            array = tmp
        return array
# @lc code=end
s = Solution()
print(s.letterCombinations(''))
