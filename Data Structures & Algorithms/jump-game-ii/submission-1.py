class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        steps = 0
        while r < n-1:
            cov_range = 0
            for i in range(l, r+1):
                cov_range = max(cov_range, i+nums[i])
            l = r+1
            r = cov_range
            steps = steps + 1
        return steps
        