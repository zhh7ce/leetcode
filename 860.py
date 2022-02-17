#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
from typing import List
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five:
                    if ten:
                        five -= 1
                        ten -= 1
                    elif five >= 3:
                        five -=3
                    else:
                        return False
                else:
                    return False
        return True
# @lc code=end

l = [5,5,10,10,20]
s = Solution()
print(s.lemonadeChange(l))
