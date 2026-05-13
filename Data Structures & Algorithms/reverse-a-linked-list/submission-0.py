class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        stack = []
        while current is not None:
            stack.append(current)
            current = current.next
        new = stack.pop()
        curr = new
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        
        return new