class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to hold the start of the merged list
        dummy = ListNode()
        tail = dummy

        # While both lists have nodes remaining
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward
            tail = tail.next

        # If one list is longer than the other, attach the remainder
        # (Since the lists are sorted, the remainder is already in order)
        tail.next = list1 if list1 else list2

        # Return the actual head (skipping the dummy node)
        return dummy.next
