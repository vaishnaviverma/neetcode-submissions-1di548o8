class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temps) 
        for i, v in enumerate(temps):
            while stack and stack[-1][0]<v:
                curr_val, curr_idx = stack.pop()
                ans[curr_idx] = i-curr_idx
            stack.append([v,i])
        return ans