class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = sorted(s)
        chars2 = sorted(t)

        return chars == chars2
