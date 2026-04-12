class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Brute Force"""
        max_sum = -math.inf
        n = len(nums)
        cumsum = [0] * n
        cumsum[0]=nums[0]
        for k in range(1,n):
            cumsum[k] = cumsum[k-1]+nums[k]
        for i in range(n): 
            for j in range(0, i+1):
                curr_sum = cumsum[i]-cumsum[j]+nums[j]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum