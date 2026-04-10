class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        check = {}
        def dfs(curr_sum, i):
            if i == l:
                if curr_sum==target:
                    return 1
                return 0 
            if (curr_sum, i) in check:
                return check[(curr_sum, i)]
            check[(curr_sum, i)] = dfs(curr_sum-nums[i], i+1) + dfs(curr_sum+nums[i], i+1)
            return check[(curr_sum, i)]
        
        count = dfs(0,0)
        return count