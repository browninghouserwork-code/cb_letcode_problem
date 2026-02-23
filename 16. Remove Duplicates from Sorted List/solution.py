# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start a pointer called `current` at the head of the linked list
        current = head 
        
        # Traverse the list while there is a current node and a next node to compare
        while current and current.next:
            if current.val == current.next.val:
                # Remove the duplicate by skipping the next node
                current.next = current.next.next
            else:
                current = current.next
        # Return the head of the updated linked list (duplicates removed)
        return head
