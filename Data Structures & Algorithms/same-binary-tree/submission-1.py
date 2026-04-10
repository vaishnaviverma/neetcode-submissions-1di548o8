# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, np: Optional[TreeNode], nq: Optional[TreeNode]) -> bool:
        if (np and not nq) or (nq and not np):
            return False
        if not np and not nq:
            return True
        if  np.val!=nq.val:
            return False
        # self.isSameTree(np.left, nq.left)
        # self.isSameTree(np.right, nq.right)
        return self.isSameTree(np.left, nq.left) and self.isSameTree(np.right, nq.right)