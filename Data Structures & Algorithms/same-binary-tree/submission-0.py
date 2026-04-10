# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        def check(np, nq):
            nonlocal ans
            if (np and not nq) or (nq and not np):
                ans = False
                return
            if not np and not nq:
                return
            if  np.val!=nq.val:
                ans = False
                return 
            check(np.left, nq.left)
            check(np.right, nq.right)
        check(p,q)
        return ans