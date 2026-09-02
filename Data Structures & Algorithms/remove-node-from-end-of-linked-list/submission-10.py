# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        
        curr = head
        while curr :
            length += 1
            curr = curr.next
        node_index = length - n

        prev = None
        curr = head
        i = 0
        while i != node_index and curr:
            prev = curr
            curr = curr.next
            i += 1
    
     
        if i == 0:
            head = curr.next
        else:
            prev.next = curr.next
        return head













        