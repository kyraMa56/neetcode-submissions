class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}

        for bracket in s:
            if bracket in pairs:
                if stack and pairs[bracket] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(bracket)
        
        return not stack