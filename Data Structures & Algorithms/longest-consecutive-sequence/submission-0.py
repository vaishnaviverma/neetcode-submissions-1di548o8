class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            streak=0
            curr=num
            while curr in nums:
                curr+=1
                streak+=1
            ans=max(ans,streak)
        return ans
        