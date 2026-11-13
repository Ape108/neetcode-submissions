from heapq import heapify, heappop, heappush
from math import sqrt

class Solution:
    def euclidean(self, point):
        x = point[0]
        y = point[1]
        return (sqrt(x**2 + y**2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            dist = self.euclidean(p)
            heappush(distances, (dist, p))
        k_closest = []
        while k > 0:
            closest = heappop(distances)
            k_closest.append(closest[1])
            k -= 1
        return k_closest


        