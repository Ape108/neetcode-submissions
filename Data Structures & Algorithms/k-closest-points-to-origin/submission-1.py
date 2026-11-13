from heapq import heapify, heappop, heappush
from math import sqrt

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            distances.append((dist, p))
        heapify(distances)
        k_closest = []
        while k > 0:
            closest = heappop(distances)
            k_closest.append(closest[1])
            k -= 1
        return k_closest


        