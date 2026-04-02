class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
      self.left = ListNode(-1)
      self.right = ListNode(-1)
      self.left.next = self.right
      self.left.prev=None
      self.right.prev=self.left
      self.right.next=None

    def isEmpty(self) -> bool:
        if(self.left.next is self.right):
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
    
        newNode = ListNode(value)
        prevNode = self.right.prev
        prevNode.next=newNode
        newNode.prev=prevNode
        newNode.next=self.right
        self.right.prev=newNode
    
        

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        nextNode = self.left.next
        self.left.next = newNode
        newNode.next = nextNode
        nextNode.prev= newNode
        newNode.prev=self.left
    
        

    def pop(self) -> int:
        if(self.left.next is self.right):
            return -1
        else:
            prevNode = self.right.prev
            newLast= prevNode.prev
            newLast.next = self.right
            self.right.prev= newLast

            return prevNode.val


        

    def popleft(self) -> int:
        if(self.left.next is self.right):
            return -1
        else:
            nextNode = self.left.next
            newFirst= nextNode.next
            newFirst.prev=self.left
            self.left.next=newFirst
           

            return nextNode.val
        
