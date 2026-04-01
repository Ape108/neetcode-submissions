class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totals_dict = {}
        for i in range(len(nums)):
            j = 0
            total = nums[j]
            j += 1
            while j < i:
                total *= nums[j]
                j += 1
            j = i + 1
            while j < len(nums):
                total *= nums[j]
                j += 1
            if i == 0:
                if nums[0] != 0:
                    total /= nums[0]
                    total = int(total)

            totals_dict[i] = total

        output = [i for i in totals_dict.values()]
        return output