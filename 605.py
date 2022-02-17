#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        flowerbed.append(1)
        count = 0
        answer = 0
        for i in flowerbed:
            if i == 0:
                count += 1
            else:
                if count == 0:
                    continue
                else:
                    answer += (count - 1) // 2
                    count = 0
        return answer >= n

# @lc code=end

