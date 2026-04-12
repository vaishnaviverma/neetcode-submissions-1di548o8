class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cov_range = 0
        for i in range(n):
            if i >cov_range:
                return False
            cov_range = max(cov_range, nums[i]+i)
            if cov_range >= n-1:
                return True