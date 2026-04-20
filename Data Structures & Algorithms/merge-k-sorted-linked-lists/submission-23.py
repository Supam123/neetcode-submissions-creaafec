# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      if lists is None or len(lists) == 0:
        return None

      def mergeList(l1,l2):
        dummyNode = ListNode()
        ptr = dummyNode
        while l1 and l2:
          if l1.val < l2.val:
            ptr.next = l1
            ptr = l1
            l1 = l1.next
          else:
            ptr.next = l2
            ptr = l2
            l2 = l2.next
        if l1 is None:
          ptr.next = l2
        if l2 is None:
          ptr.next = l1
        return dummyNode.next

      while len(lists) > 1:
        temp = []
        for i in range(0,len(lists),2):
          l1 = lists[i] if i < len(lists) else None
          l2 = lists[i+1] if i+1 < len(lists) else None
          temp.append(mergeList(l1,l2))
        lists = temp
      return lists[0]
      




