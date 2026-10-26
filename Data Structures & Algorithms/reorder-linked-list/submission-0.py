# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        beginning = head

        while beginning:
            end = beginning
            while end and end.next:
                prev_end = end
                end = end.next
            if end == beginning:
                return
            if end == beginning.next:
                return
            beg_nxt = beginning.next 
            beginning.next = end # 4 -> 6
            end.next = beg_nxt # 6 -> 4
            prev_end.next = None
            beginning = beg_nxt
        
        

# one pointer -> beginning
# one pointer -> at the end O(n)
# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# 0 -> 5 