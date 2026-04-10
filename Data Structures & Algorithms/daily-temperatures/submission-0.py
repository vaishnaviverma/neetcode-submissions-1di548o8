class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = []
        for i in range(len(temps)):
            curr = temps[i]
            flag=0
            for j in range(i+1, len(temps)):
                if temps[j]>curr:
                    ans.append(j-i)
                    flag=1
                    break
            if flag==0:
                ans.append(0)
        return ans