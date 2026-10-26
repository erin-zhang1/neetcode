class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for i in s:
            if i not in s_set:
                s_set[i] = 0
            s_set[i] += 1
        for j in t:
            if j not in t_set:
                t_set[j] = 0
            t_set[j] += 1
        
        return s_set == t_set

        