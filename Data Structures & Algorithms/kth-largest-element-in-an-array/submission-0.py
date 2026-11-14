import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k > 0:
            largest = heapq.heappop_max(nums)
            k -= 1
        return largest
        