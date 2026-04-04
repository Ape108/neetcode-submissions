class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        if len(piles) == h:
            return max_val
        
        l, r = 1, max_val
        while l <= r:
            mid = (l + r) // 2 # Current k

            time = sum((p - 1) // mid + 1 for p in piles)

            if time <= h:
                r = mid - 1 # try a smaller k
            else: # k isn't fast enough
                l = mid + 1 # try a bigger k
            
        return l

            




    

        
        