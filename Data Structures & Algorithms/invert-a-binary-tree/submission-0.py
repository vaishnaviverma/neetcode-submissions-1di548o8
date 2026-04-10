# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swapnodes(curr_root):
            if curr_root is None:
                return
            temp = curr_root.left
            curr_root.left = curr_root.right
            curr_root.right = temp
            swapnodes(curr_root.left)
            swapnodes(curr_root.right)
        ans_root = root
        swapnodes(root)
        return ans_root