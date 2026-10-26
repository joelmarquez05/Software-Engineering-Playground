# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stored_nodes = set()
        curr = head

        while curr:
            if curr in stored_nodes:
                break
            stored_nodes.add(curr)
            curr = curr.next
        if curr:
            return True
        else:
            return False
