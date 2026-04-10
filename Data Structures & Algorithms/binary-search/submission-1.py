class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        l , h = 0 , l-1
        
        while(l<=h):
            mid = l + int((h-l)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1
        