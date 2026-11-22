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
    int goodNodes(TreeNode* root) {
        // bfs, keep track of max value seen in this search
        // if we encounter a new node greater, update max, keep searching
        int count = 0;
        int max = root->val;
        dfs(root, count, max);
        return count;
    }

    void dfs(TreeNode* root, int& count, int max) {
        if (!root) return;
        if (root->val >= max) {
            max = root->val;
            count++;
        }
        dfs(root->left, count, max);
        dfs(root->right, count, max);
        return;
    }
};
