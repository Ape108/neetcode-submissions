class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 
        freq_count = {}
        l = 0
        max_f = 0

        for r in range(len(s)):
            freq_count[s[r]] = freq_count.get(s[r], 0) + 1

            max_f = max(max_f, freq_count[s[r]])

            while (r - l + 1) - max_f > k:
                freq_count[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len


            
