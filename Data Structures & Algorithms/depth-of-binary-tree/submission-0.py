# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_d = 0
        def dfs(curr_node, curr_d):
            nonlocal max_d
            if curr_node is None:
                return
            if curr_node.left is None and curr_node.right is None:
                max_d
                max_d = max(max_d, curr_d)
                return
            dfs(curr_node.left, curr_d+1)
            dfs(curr_node.right, curr_d+1)

        dfs(root, 0)
        return max_d+1
        