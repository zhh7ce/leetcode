/*
 * @lc app=leetcode.cn id=474 lang=cpp
 *
 * [474] 一和零
 */

// @lc code=start
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int number = strs.size();
        int zero[number];
        int one[number];
        for (int item = 0; item < number; ++item) {
            zero[item] = 0;
            one[item] = 0;
        }
        for (int item = 0; item < number; ++item) {
            for (int cha = 0; cha < strs[item].size(); ++cha) {
                if (strs[item][cha] == '0') {
                    ++zero[item];
                } else {
                    ++one[item];
                }
            }
        }
        int dp[m+1][n+1];
        for (int mWeight = m; mWeight >= 0; --mWeight) {
            for (int nWeight = n; nWeight >= 0; --nWeight) {
                if (mWeight >= zero[0] && nWeight >= one[0]) {
                    dp[mWeight][nWeight] = 1;
                } else {
                    dp[mWeight][nWeight] = 0;
                }
            }
        }
        for (int item = 1; item < number; ++item) {
            for (int mWeight = m; mWeight >= 0; --mWeight) {
                for (int nWeight = n; nWeight >= 0; --nWeight) {
                    if (mWeight >= zero[item] && nWeight >= one[item]) {
                        dp[mWeight][nWeight] = max(dp[mWeight][nWeight], 1+dp[mWeight-zero[item]][nWeight-one[item]]);
                    }
                }
            }
        }
        return dp[m][n];
    }
};
// @lc code=end

