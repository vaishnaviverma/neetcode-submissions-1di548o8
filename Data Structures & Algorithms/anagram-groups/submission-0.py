class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()
        for s in strs:
            s_ana = "".join(sorted(s))
            if s_ana in data:
                data[s_ana].append(s)
            else:
                data[s_ana]=[s]
        return list(data.values())
        