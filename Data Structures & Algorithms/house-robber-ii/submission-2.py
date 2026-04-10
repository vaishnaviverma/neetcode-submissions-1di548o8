class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[:-1]
        nums2 = nums[1:]
        n = len(nums1)
        if len(nums)<=1:
            return nums[0]
        elif len(nums)<=2:
            return max(nums[1], nums[0])
        ans1 = [-1]*(n)
        ans1[0]=nums1[0]
        ans1[1]=max(nums1[0],nums1[1])
        for i in range(2, n):
            ans1[i] = max(nums1[i]+ans1[i-2], ans1[i-1])
        ans2 = [-1]*(n)
        ans2[0]=nums2[0]
        ans2[1]=max(nums2[0],nums2[1])
        for i in range(2, n):
            ans2[i] = max(nums2[i]+ans2[i-2], ans2[i-1])
        return max(ans1[n-1],ans2[n-1])