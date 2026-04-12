class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [math.inf] * n
        # curr_step = 0
        pos[0] = 0
        for i in range(n):
            for j in range(nums[i]+1):
                if i+j<n:
                    pos[i+j] = min(pos[i+j], pos[i]+1)
        return pos[-1]
        