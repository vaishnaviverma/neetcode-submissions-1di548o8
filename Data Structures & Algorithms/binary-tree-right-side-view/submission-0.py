# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs_arr = {}
        def bfs(curr_node, level):
            nonlocal bfs_arr
            if not curr_node:
                return
            if len(bfs_arr)==level:
                bfs_arr[level]=[]
            bfs_arr[level].append(curr_node.val)
            bfs(curr_node.left, level+1)
            bfs(curr_node.right, level+1)
        bfs(root, 0)
        ans=[]
        for val in bfs_arr.values():
            ans.append(val[-1])
        return ans
        