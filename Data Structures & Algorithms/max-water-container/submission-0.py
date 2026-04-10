class Solution:
    def maxArea(self, nums: List[int]) -> int:
        size = len(nums)
        l = 0
        r = size-1
        max_water = 0
        while(l<r):
            curr_water = min(nums[l],nums[r]) * (r-l)
            max_water = max(curr_water, max_water)
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return max_water
        