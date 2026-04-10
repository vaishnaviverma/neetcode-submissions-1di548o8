# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = {}
        def bfs(curr_node, level):
            nonlocal ans
            if not curr_node:
                return
            ans[level] = ans.get(level,[])
            ans[level].append(curr_node.val)
            bfs(curr_node.left, level+1)
            bfs(curr_node.right, level+1)
        bfs(root, 0)
        ans2 = []
        for val in ans.values():
            ans2.append(val)
        return ans2

        