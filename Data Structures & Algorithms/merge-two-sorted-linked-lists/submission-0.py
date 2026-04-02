# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def append(self,newNode):

        if(self.head is None and self.rear is None):
            self.head =  newNode
            self.rear = newNode
        elif(self.head == self.rear):
            self.head.next = newNode
            self.rear= newNode
        else:
            self.rear.next = newNode
            self.rear =  newNode
        

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        target =  LinkedList()
        while current1 is not None and current2 is not None:
            if(current1.val == current2.val):
                target.append(current1)
                current1 = current1.next
            elif(current1.val <current2.val):
                target.append(current1)
                current1=current1.next
            else:
                target.append(current2)
                current2 =current2.next
        if(current1 is None and current2 is not None):
            while(current2 is not None):
                target.append(current2)
                current2=current2.next
        if(current1 is not None and current2 is None):
            while(current1 is not None):
                target.append(current1)
                current1=current1.next
        
        return target.head