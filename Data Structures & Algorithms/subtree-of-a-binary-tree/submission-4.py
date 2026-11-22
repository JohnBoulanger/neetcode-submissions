# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        found = False

        def isEqual(p, q):
            # base cases
            if not p and not q: return True
            if not p and q or not q and p: return False
            if p.val != q.val: return False

            # dfs comparison on subtrees
            return isEqual(p.left, q.left) and isEqual(p.right, q.right)
        
        def dfs(root, subRoot):
            if not root or not subRoot: return

            # compare current nodes children with subroots children to see if we have a match
            nonlocal found
            if root.val == subRoot.val and isEqual(root, subRoot):
                found = True

            # dfs
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)

            return

        dfs(root, subRoot)
        return found

            