# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = ListNode()
        current = list3

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp = list1.next
                current.next = list1
                list1 = temp
                current = current.next
            elif list2.val <= list1.val:
                temp = list2.next
                current.next = list2
                list2 = temp
                current = current.next
        
        if list1 is None:
            current.next = list2
        else:
            current.next = list1
        
        return list3.next




