class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'{':'}', '[':']', '(':')'}
        stack = []
        for char in s:
            if char in opening.keys():
                stack.append(char)
            elif char in opening.values():
                if not stack:
                    return False
                check = stack.pop()
                if opening[check] != char:
                    return False
        
        if stack:
            return False
        return True
