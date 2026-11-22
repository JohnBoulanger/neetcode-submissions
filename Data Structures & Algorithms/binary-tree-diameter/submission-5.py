# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # length = depth of left subtree + depth of right subtree
        def depthOfSubtree(root):
            if not root: return 0
            return 1 + max(depthOfSubtree(root.left), depthOfSubtree(root.right))

        diameterOfNode = depthOfSubtree(root.left) + depthOfSubtree(root.right)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right),
                    diameterOfNode)

