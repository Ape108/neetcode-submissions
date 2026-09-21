class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x, y)
            if x != y:
                if x < y:
                    heapq.heappush(stones, x - y)
                else:
                    heapq.heappush(stones, y - x)
            heapq.heapify(stones)
            
        if not stones:
            return 0
        else:
            return -stones[0]

