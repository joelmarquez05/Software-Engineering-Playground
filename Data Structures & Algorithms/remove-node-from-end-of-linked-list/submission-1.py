# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4 -> 5  # length = 5
                         # length - n

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        node_before = dummy
        for _ in range(length - n):
            node_before = node_before.next

        node_before.next = node_before.next.next
        return dummy.next

        
        





    
        