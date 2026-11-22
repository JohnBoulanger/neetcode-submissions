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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // search until you find the node between/equal to the values p and q,
        // that is yur ancestor bbyyyyyyyy
        TreeNode* cur = root;
        while(1) {
            if (cur->val >= p->val && cur->val <= q->val
                || cur->val <= p->val && cur->val >= q->val) return cur;
            if (cur->val > p->val && cur->val > q->val) cur = cur->left;
            else cur = cur->right;
        }
        return nullptr;
    }
};
