class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]
        count=0
        for i in range(l, -1, -1):
            for j in range(i,l):
                if s[i]==s[j]:
                    if(j-i<=2 or dp[i+1][j-1]):
                        dp[i][j]=True
                        count+=1
        return count
        
