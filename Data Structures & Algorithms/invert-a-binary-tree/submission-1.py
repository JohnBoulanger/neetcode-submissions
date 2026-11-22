# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and (root.right or root.left):
            # swap child nodes
            temp = root.right
            root.right = root.left
            root.left = temp
            # recurse and swap on children
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root
        
        