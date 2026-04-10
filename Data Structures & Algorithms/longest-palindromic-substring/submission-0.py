class Solution:
    def helper(self, s):
        l = len(s)
        for i in range(l):
            if s[i]!=s[l-i-1]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        maxlen=1
        ansstr = s[0]
        l = len(s)
        for i in range(l):
            for j in range(i+1, l):
                substr=s[i:j+1]
                if self.helper(substr):
                    if len(substr)>maxlen:
                        maxlen=len(substr)
                        ansstr=substr
        return ansstr

        