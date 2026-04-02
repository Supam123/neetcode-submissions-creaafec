# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        pointer = dummyNode
        curr1 = list1
        curr2 = list2
        while(curr1 and curr2):
            if(curr1.val<curr2.val):
                pointer.next = curr1
                curr1 = curr1.next
            else:
                pointer.next = curr2
                curr2 = curr2.next
            pointer = pointer.next
        
        if(curr1 is None):
            pointer.next = curr2
        elif(curr2 is None):
            pointer.next = curr1
        return dummyNode.next 
     