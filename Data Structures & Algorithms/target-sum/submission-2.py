class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        l = len(nums)
        def dfs(curr_sum, i):
            nonlocal count
            if i == l:
                if curr_sum==target:
                    count+=1
                return
            dfs(curr_sum-nums[i], i+1)
            dfs(curr_sum+nums[i], i+1)
        
        dfs(0,0)
        return count