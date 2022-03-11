/*
 * @lc app=leetcode.cn id=2049 lang=cpp
 *
 * [2049] 统计最高分的节点数目
 */

#include<vector>
using namespace std;
// @lc code=start
typedef struct node{
    node* left = nullptr;
    node* right = nullptr;
    int left_count = 0;
    int right_count = 0;
} *ptr;

class Solution {
public:
    long _max = -1;
    int _count = 0;
    long _n = 0;
    int countHighestScoreNodes(vector<int>& parents) {
        long n = parents.size();
        this->_n = n;
        this->_max = -1;
        this->_count = 0;
        ptr tree[n];
        for (long i = 0; i < n; i++) {
            tree[i] = new node();
        }
        for (long i = 1; i < n; i++) {
            if (tree[parents[i]]->left == nullptr) {
                tree[parents[i]]->left = tree[i];
            } else {
                tree[parents[i]]->right = tree[i];
            }
        }
        count(tree[0]);
        return this->_count;
    }

    void count(ptr node) {
        long score = 1;
        if (node->left != nullptr) {
            count(node->left);
            node->left_count = node->left->left_count + node->left->right_count + 1;
            score *= node->left_count;
        }
        if (node->right != nullptr) {
            count(node->right);
            node->right_count = node->right->left_count + node->right->right_count + 1;
            score *= node->right_count;
        }
        score *= max(long(1), _n - node->left_count - node->right_count -1);
        if (score > _max) {
            _max = score;
            _count = 1;
        } else if (score == _max) {
            _count++;
        }
    }
};
// @lc code=end

