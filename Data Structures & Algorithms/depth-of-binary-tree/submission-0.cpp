/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // base case
        if (!root) return 0;
        
        int leftDepth = 1;
        int rightDepth = 1;
        TreeNode* cur = root;
        if (root->left){
            leftDepth += maxDepth(cur->left);
        }
        if (root->right) {
            rightDepth += maxDepth(cur->right);
        }

        return std::max(leftDepth, rightDepth);
    }
};
