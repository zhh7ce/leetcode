/*
 * @lc app=leetcode.cn id=1025 lang=cpp
 *
 * [1025] 除数博弈
 */

// @lc code=start
class Solution {
public:
    bool divisorGame(int N) {
        bool dp[N+1]; // shows in your turn
        dp[0] = false;
        dp[1] = false;
        for (int number = 2; number <= N; ++number) {
            dp[number] = false;
            for (int factor = 1; factor < number; ++factor) {
                if (number % factor == 0 && dp[number-factor] == false) {
                    dp[number] = true;
                    break;
                }
            }
        }
        return dp[N];
    }
};
// @lc code=end

