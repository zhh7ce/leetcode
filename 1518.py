import sys

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        emptyBottles = 0
        while numBottles:
            result += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange
            emptyBottles %= numExchange
        return result

sol = Solution()
print(sol.numWaterBottles(int(sys.argv[1]), int(sys.argv[2])))