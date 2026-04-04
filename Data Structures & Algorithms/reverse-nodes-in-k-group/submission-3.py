# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        groupPrev = dummyNode
        while True:
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummyNode.next # basically we are done
            
            #after this loop k lands on the kth node
            tail = groupPrev.next
            temp = kth.next

            prev = temp
            curr= tail
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            groupPrev.next = kth
            groupPrev = tail
        return dummyNode.next

            

        