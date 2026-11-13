from heapq import heapify, heappop, heappush
from math import sqrt

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            distances.append([dist, [x, y]])
        heapify(distances)
        k_closest = []
        while k > 0:
            closest = heappop(distances)
            k_closest.append(closest[1])
            k -= 1
        return k_closest


        