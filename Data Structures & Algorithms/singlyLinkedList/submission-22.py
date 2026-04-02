class LinkedNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head         

    
    def get(self, index: int) -> int:
        
        curr = self.head.next
        i = 0
        while curr is not None:
            if(i == index):
                return curr.val
            i+=1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node  = LinkedNode(val)
        new_node.next = self.head.next # head is always dummy
        self.head.next = new_node # linking dummy with new node
        if(new_node.next is None): # meaning only one node
            self.tail = new_node
        
        

    def insertTail(self, val: int) -> None:
        new_node = LinkedNode(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head # not head.nmext cuz we want the node before the one we wanna delete
        while i < index and curr is not None:
            i +=1
            curr =  curr.next
        
        #then we have reached the i and the curr is node before i
        if curr and curr.next:
            if(curr.next == self.tail):
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
       

        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr is not None:
            res.append(curr.val)
            curr = curr.next 
        return res
        
