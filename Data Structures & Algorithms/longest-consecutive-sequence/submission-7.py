class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                count = 1
                while n + 1 in nums_set:
                    count += 1
                    n += 1
                if count > result:
                    result = count
        return result







