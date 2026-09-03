class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        l = 0
        result = []
        max_val = nums[0]
        max_idx = 0
        for i in range(l, k):
            if nums[i] >= max_val:
                max_val = nums[i]
                max_idx = i
        
        result.append(max_val)
        
        for r in range(k, len(nums)):
            incoming = nums[r]
            if incoming >= max_val:
                max_val = incoming
                max_idx = r
            else: # incoming < max_val
            # is the current max outgoing? otherwise carry on.
                if l == max_idx:
                    # now we have to find the new max
                    new_val = nums[l + 1] 
                    new_idx = l + 1
                    for i in range(l + 2, r + 1):
                        if nums[i] >= new_val:
                            new_val = nums[i]
                            new_idx = i
                    max_val = new_val
                    max_idx = new_idx
            
            result.append(max_val)

            l += 1 

        return result

        