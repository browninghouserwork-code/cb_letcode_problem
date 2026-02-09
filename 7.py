class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        values = []
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next

        values.sort()
        
        dummy = ListNode()
        current = dummy

        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
