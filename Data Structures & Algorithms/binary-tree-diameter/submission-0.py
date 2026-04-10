# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def dfs(curr_node):
            nonlocal max_d
            if curr_node is None:
                return 0
            
            left_d = dfs(curr_node.left)
            right_d = dfs(curr_node.right)
            curr_d = left_d + right_d
            max_d = max(max_d, curr_d)
            return 1 + max(left_d, right_d)
        
        dfs(root)
        return max_d