class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr :
            if(i ==  index):
                return curr.val
            i +=1
            curr = curr.next
        return  -1
        

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        if(new.next == None):
            self.tail = new
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i +=1
            curr = curr.next
        if curr and curr.next:
             if(curr.next == self.tail):
                self.tail = curr
             curr.next = curr.next.next
             return True
        return False
             
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr :
            res.append(curr.val)
            curr = curr.next
        return res

        
