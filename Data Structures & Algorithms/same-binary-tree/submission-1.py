# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        same = True
        # dfs only change to false if l1 != l2 or r1 != l2
        def dfs(p, q):
            # both None which is equal
            if not p and not q: return

            nonlocal same
            # one of the two is None
            if (p and not q) or (q and not p):
                same = False
                return

            # values dont match
            if p.val != q.val:
                same =  False

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return same
            