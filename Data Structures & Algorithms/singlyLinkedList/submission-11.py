class ListNode:
    def __init__(self,val):
        self.value =val
        self.next = None

class LinkedList:
    
    def __init__(self):
       self.head = None
       self.tail = None

    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr != None:
            if(i == index):
                return curr.value
            else:
                curr= curr.next
                i+=1
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if(self.head == None and self.tail ==None):
            self.head =new_node
            self.tail =new_node
            new_node.next = None

        else:
            new_node.next = self.head
            self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if(self.head == None and self.tail ==None):
            self.head =new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        prev =  self.head
        curr=  self.head
        i = 0
    
        if (index == 0):
            self.head=self.head.next
            if(self.head is None):
                self.tail=None
            return True
     
        while curr!=None:
            if(i == index):
                prev.next = curr.next
                if(curr.next == None):
                    self.tail = prev
                return True
            else:
                prev =curr
                curr = curr.next
                i+=1
        return False

        

    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res



















        
