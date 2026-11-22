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
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        // root recieves maximum difference between heights in left and right subtrees
        int result = 0;
        dfs(root, result);
        return result > 1 ? false : true;
        
    }

    int dfs(TreeNode* root, int& result){
        if (!root) return 0;
        // get subtree heights for l and r nodes
        int left = dfs(root->left, result);
        int right = dfs(root->right, result);
        // for this particular node, get the difference in heights between l and r
        // keep the maximum
        result = std::max(result, std::abs(left - right));
        // return maximum subtree height between left and right + 1 to parent
        return 1 + std::max(left, right); 
    }
};
