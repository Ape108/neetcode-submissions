import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tail = dummy = ListNode()

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)
        
        while heap:
            smallest = heapq.heappop(heap)

            tail.next = smallest
            tail = tail.next

            if smallest.next:
                heapq.heappush(heap, smallest.next)

        return dummy.next
        