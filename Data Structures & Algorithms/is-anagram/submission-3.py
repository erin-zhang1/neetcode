from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = Counter(s)
        t_frequency = Counter(t)

        if s_frequency == t_frequency:
            return True
        return False
        
