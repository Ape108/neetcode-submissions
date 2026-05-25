class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        curr = head
        count = 0
        if count == (size - n):
            return head.next
        while count + 1 != (size - n):
            if curr.next is None: 
                curr = head # cycle back to head while incrementing count
            else: 
                curr = curr.next
            count += 1
        if curr.next is None:
            # the head is the node to be removed
            return head.next
        next = curr.next
        curr.next = curr.next.next
        next.next = None
        return head
        

        
