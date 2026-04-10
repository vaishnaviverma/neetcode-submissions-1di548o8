class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        elif l==2:
            return max(nums[0],nums[1])
        robs = [-1] * l
        robs[0] = nums[0]
        robs[1] = max(nums[0],nums[1])
        for i in range(2,l):
            robs[i] = max(nums[i]+robs[i-2], robs[i-1])
        return robs[l-1]
