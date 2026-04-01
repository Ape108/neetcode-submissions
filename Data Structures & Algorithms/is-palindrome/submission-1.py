class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ""
        for c in s:
            if c.isalnum():
                target += c.lower()
        reverse = target[::-1]
        for i in range(len(target)):
            if target[i] != reverse[i]:
                return False

        return True