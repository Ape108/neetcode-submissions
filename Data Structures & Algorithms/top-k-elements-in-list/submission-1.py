class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []

        for n in nums:
            counts[n] += 1
        
        res = list(counts.items())
        res.sort(key=lambda x: x[1], reverse=True)
        res = res[0:k]
        return [key for key, val in res]
            

