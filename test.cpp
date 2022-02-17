#include <iostream>
#include <vector>
using namespace std;

void printArr(int nums[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << nums[i] << ' ';
    }
    cout << endl;
}

void print2DArr(int dp[5][3], int m, int n) {
    for (int mWeight = 0; mWeight < m; ++mWeight) {
        for (int nWeight = 0; nWeight < n; ++nWeight) {
            cout << dp[mWeight][nWeight] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    TreeNode* convertBiNode(TreeNode* root) {
        if (not root) {
            return root;
        }
        TreeNode* newRoot = root;
        if (root->left) {
            newRoot = convertBiNode(root->left);
            TreeNode* tmp = newRoot;
            while (tmp->right) {
                tmp = tmp->right;
            }
            tmp->right = root;
        }
        TreeNode* right = convertBiNode(root->right);
        root->right = right;
        // TreeNode* tmp = newRoot;
        // while (tmp) {
        //     cout << tmp->val << ' ';
        //     tmp = tmp->right;
        // }
        cout << endl;
        return newRoot;
    }
};

int main(){
    TreeNode t = TreeNode(1);
    t.left = TreeNode(0);
    t.right = TreeNode(2);
    Solution s = Solution();
    cout << s.convertBiNode(&t);
    return 0;
}