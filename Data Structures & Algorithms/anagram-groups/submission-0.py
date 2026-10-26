class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dics = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dics:
                dics[key] = []
            dics[key].append(s) # .append does not return value, it only modified the list
        return list(dics.values())

