# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        ptr = dummyNode
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:

            if curr1.val <= curr2.val:
                ptr.next = curr1
                ptr = curr1
                curr1 = curr1.next
            else:
                ptr.next = curr2
                ptr = curr2
                curr2 = curr2.next
            
        if curr1 is None:
            ptr.next = curr2
        else:
            ptr.next =  curr1
        return dummyNode.next



        