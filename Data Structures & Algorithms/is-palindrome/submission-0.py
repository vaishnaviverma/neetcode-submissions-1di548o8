class Solution:
    def isPalindrome(self, text: str) -> bool:
        s = ''
        for c in text:
            if c.isalnum():
                s+=c.lower()
        l = 0
        r = len(s)-1
        while(l<r):
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        