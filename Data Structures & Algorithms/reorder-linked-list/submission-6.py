# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

  
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        find the middle using fast and slow pointers spearte two lists
        reverse the second lsit 5->4->3
        then merge the first half with the second half
        '''
        
        # finding middle and splitting them in two
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is sitting at the middle
        head2 = slow.next 
        slow.next =  None
        # after this head 1 ------ slow  = list 1
        # head2 till none is = list 2


        # reverse list 2
        prev,curr = None,head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # after the list is revresed prev will be head
        # final step merge first half and reveresd half together

        curr1 = head
        curr2 = prev
        ptr = curr1
        while curr1 and curr2:
            curr1 = curr1.next
            ptr.next =  curr2
            ptr = curr2
            curr2 = curr2.next
            ptr.next = curr1
            ptr = curr1
        
