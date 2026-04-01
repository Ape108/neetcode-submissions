class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ""
        for c in s:
            if c.isalnum():
                target += c.lower()
        return target == target[::-1]