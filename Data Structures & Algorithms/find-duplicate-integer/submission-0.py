class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while nums:
            val = nums.pop(i)
            if val in nums:
                return val
        return None