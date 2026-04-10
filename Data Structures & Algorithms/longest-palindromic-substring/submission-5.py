class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        # dp = [[False]*l] * l
        dp = [[False] * l for _ in range(l)]
        maxlen=0
        maxidx=0
        # for i in range(l):
        #     dp[i][i]=True
        for i in range(l - 1, -1, -1):
            for j in range(i,l):
                if s[i]==s[j]:
                    if j-i<=2 or dp[i+1][j-1]:
                        dp[i][j]=True
                        if (j-i+1)>maxlen:
                            maxlen=(j-i+1)
                            maxidx=i
        return s[maxidx:maxidx+maxlen]