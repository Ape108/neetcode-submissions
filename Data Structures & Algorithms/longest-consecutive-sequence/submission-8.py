class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                count = 0
                while (n + count) in nums_set:
                    count += 1
                result = max(result, count)
        return result







