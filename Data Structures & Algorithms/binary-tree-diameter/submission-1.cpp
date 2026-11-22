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
        if (!root) return 0;

        int leftDepth = 1;
        int rightDepth = 1;
        if (root->left) {
            leftDepth += maxDepth(root->left);
        }
        if (root->right) {
            rightDepth += maxDepth(root->right);
        }
        return std::max(leftDepth, rightDepth);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        // for all nodes, maximum of max depth left + max depth right = total diameter
        if (!root) return 0;

        // init
        int leftDepth = 0;
        int rightDepth = 0;

        int bestDiameter = 0;

        // has left/right node
        if (root->left)
            leftDepth = maxDepth(root->left);
        if (root->right)
            rightDepth = maxDepth(root->right);

        bestDiameter = leftDepth + rightDepth;

        return std::max(bestDiameter, std::max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)));
        
    }
};
