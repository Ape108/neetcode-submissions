class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        if len(piles) == h:
            return max_val
        
        min_k = max_val
        l, r = 1, max_val
        while l <= r:
            mid = (l + r) // 2 # Current k

            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time <= h:
                if mid < min_k:
                    min_k = mid # update because k is valid
                r = mid - 1 # try a smaller k
            else: # k isn't fast enough
                l = mid + 1 # try a bigger k
            
            mid = (l + r) // 2
        
        return min_k

            




    

        
        