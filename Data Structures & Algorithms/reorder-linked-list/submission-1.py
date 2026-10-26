class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the end of the first half
        middle = head
        fast = head.next

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        # 2. Separate the two halves
        curr = middle.next
        middle.next = None

        # 3. Reverse the second half
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # At this point:
        #
        # first half:  head -> ...
        # second half: prev -> ... (reversed)

        # 4. Merge both halves
        first_half = head
        second_half = prev

        while second_half:
            # Save next nodes
            first_half_next = first_half.next
            second_half_next = second_half.next

            # Interleave
            first_half.next = second_half
            second_half.next = first_half_next

            # Advance
            first_half = first_half_next
            second_half = second_half_next