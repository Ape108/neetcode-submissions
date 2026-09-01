class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0 
        max_f = 0
        max_len = 0
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1

            max_f = max(max_f, freq_map[s[r]])

            while (r - l + 1) - max_f > k:
                freq_map[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)

        return max_len


            
