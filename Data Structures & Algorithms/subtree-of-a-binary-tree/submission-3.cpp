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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // find node in root that matches root val in subroot
        int val = subRoot->val;
        int result = false;
        if (!root) return false;
        if (!subRoot) return true;

        // check on every node in the dfs
        if (sameTree(root, subRoot)) {
            return true;
        }
        else {
            result = isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
        }
        return result;
    }

    bool sameTree(TreeNode* a, TreeNode* b) {
        // a is the "subtree" and dictates when to stop searching potentially larger tree b
        if (!a && !b) return true;

        if (a && b && a->val == b->val) {
            return sameTree(a->left, b->left) && sameTree(a->right, b->right);
        }
        return false;
    }
};
