# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEquivalent(self, np, nq):
        if (np and not nq) or (nq and not np):
            return False
        if not np and not nq:
            return True
        if np.val!=nq.val:
            return False
        return self.isEquivalent(np.left, nq.left) and self.isEquivalent(np.right, nq.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isEquivalent(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        