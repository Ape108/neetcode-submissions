class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
            
        s1_counts = [0] * 26
        s2_counts = [0] * 26 

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1

        matches = sum(1 for i in range(26) if s1_counts[i] == s2_counts[i])
        
        for i in range(n1, n2):
            if matches == 26:
                return True

            idx_in = ord(s2[i]) - ord("a")
            s2_counts[idx_in] += 1
            if s2_counts[idx_in] == s1_counts[idx_in]:
                matches += 1
            elif s2_counts[idx_in] == s1_counts[idx_in] + 1:
                matches -= 1

            idx_out = ord(s2[i - n1]) - ord("a")
            s2_counts[idx_out] -= 1
            if s2_counts[idx_out] == s1_counts[idx_out]:
                matches += 1
            elif s2_counts[idx_out] == s1_counts[idx_out] - 1:
                matches -= 1

        return matches == 26

