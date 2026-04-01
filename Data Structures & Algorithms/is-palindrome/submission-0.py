class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = []
        regular = []
        for char in s:
            if char.isalnum():
                reverse.insert(0, char)
                regular.append(char)
        rev_str = "".join(reverse)
        reg_str = "".join(regular)
        if rev_str.lower() == reg_str.lower():
            return True
        return False