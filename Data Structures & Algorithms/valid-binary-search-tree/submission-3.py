# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # right must be greater than its parent and less than its parents max
        # left must be less than its parent but greater than its parents min

        high = float('inf')
        low = float('-inf')

        def dfs(root, high, low):
            if not root: return True

            if root.val >= high or root.val <= low:
                return False
            
            return dfs(root.left, root.val, low) and dfs(root.right, high, root.val)

        valid = dfs(root, high, low)
        return valid
        