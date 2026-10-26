import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        l = 0
        r = len(clean_text) - 1

        while l < r:
            if clean_text[l] == clean_text[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

            