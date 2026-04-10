class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        ans = 0
        l = len(s)
        i=0
        j=0
        while j<l:
            if s[j] not in check:
                check.add(s[j])
                ans = max(ans, j-i+1)
                j+=1
            else:
                while s[j] in check:
                    check.remove(s[i])
                    i+=1
        return ans
        