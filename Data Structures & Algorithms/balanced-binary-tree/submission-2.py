# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # do dfs on root node to find its length of left and right subtrees
        # if abs(left - right) <= 1, return true, otherwise return false

        def dfsLength(root):
            if not root: return 0

            left = dfsLength(root.left)
            right = dfsLength(root.right)

            return 1 + max(left, right)

        def dfs(root):
            if not root: return True

            # get length of left and right subtree
            left = dfsLength(root.left)
            right = dfsLength(root.right)

            return abs(left - right) <= 1 and dfs(root.left) and dfs(root.right)

        return dfs(root)
        

