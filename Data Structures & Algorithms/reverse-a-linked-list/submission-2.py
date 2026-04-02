# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head):
            # prev=  None
            # curr =head
            # n= head.next
            # while(n!= None):
            #     curr.next = prev
            #     prev = curr
            #     curr = n
            #     n = n.next
            # curr.next = prev
            # head = curr

            prev = None
            curr = head
            while(curr is not None):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head = prev
        return head
        