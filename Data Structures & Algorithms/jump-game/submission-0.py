class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cov_range = 0
        for i in range(n):
            if i<=cov_range:
                if i == n-1:
                    return True
                cov_range = max(cov_range, nums[i]+i)
            else:
                return False