class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        chars = sorted(s)
        chars2 = sorted(t)

        for i in range(len(s)):
            if chars[i] != chars2[i]:
                return False
        return True
