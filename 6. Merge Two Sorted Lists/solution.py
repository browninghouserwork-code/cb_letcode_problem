class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        values = []
        # Traverse the first linked list and add each value to the values list
        while list1:
            values.append(list1.val) # Add current node value to values
            list1 = list1.next # Move to the next node in list1
        # Traverse the second linked list and add each value to the values list
        while list2:
            values.append(list2.val)
            list2 = list2.next

        values.sort()
        
        dummy = ListNode()
        current = dummy

        for val in values:
            current.next = ListNode(val) # Create a new node and attach to current
            current = current.next # Move the pointer to the new node
        # Return the merged list.
        return dummy.next
