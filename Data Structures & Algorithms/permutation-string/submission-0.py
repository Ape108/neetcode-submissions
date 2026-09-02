class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        # populate map with frequency of characters in s1
        for c in s1:
            freq_map[c] = freq_map.get(c, 0) + 1

        l, r = 0, len(s1) # the sliding window will be of fixed length
        while r <= len(s2):
            sub_map = {}
            substr = s2[l:r]
            for c in substr:
                sub_map[c] = sub_map.get(c, 0) + 1

            if freq_map.items() == sub_map.items():
                return True
            
            l += 1
            r += 1
        return False


        
            