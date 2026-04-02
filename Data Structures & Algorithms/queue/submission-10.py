class ListNode:
    def __init__(self,val):
        self.value = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = None
        self.tail.next = None       

    def isEmpty(self) -> bool:
        if(self.head.next == self.tail):
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        
        newNode = ListNode(value)
        prevNode = self.tail.prev
        prevNode.next = newNode
        newNode.next = self.tail
        newNode.prev = prevNode
        self.tail.prev = newNode
     
        

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        nextNode = self.head.next
        nextNode.prev = newNode
        newNode.next = nextNode
        newNode.prev = self.head
        self.head.next = newNode


        

    def pop(self) -> int:
        if(self.head.next == self.tail):
            return -1
        removedNode = self.tail.prev
        value = removedNode.value
        prevNode = removedNode.prev
        self.tail.prev = prevNode
        prevNode.next = self.tail
        return value

        

    def popleft(self) -> int:
        if(self.head.next == self.tail):
            return -1
        removedNode = self.head.next
        value =  removedNode.value
        nextNode = removedNode.next
        self.head.next = nextNode
        nextNode.prev  = self.head
        return value
