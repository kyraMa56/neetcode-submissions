class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            elif stack and bracket == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        return False