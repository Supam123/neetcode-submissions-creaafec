class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.front = None
        self.rear = None
            
    def get(self, index: int) -> int:
        curr= self.front
        i = 0
        while(curr!=None):
            if(i==index):
                return curr.val
            else:
                i+=1
                curr=curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.front
        if(self.front is None):
            self.front=new_node
            self.rear=new_node
        else:
            self.front=new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = None
        if(self.rear is not None):
            self.rear.next = new_node
            self.rear= new_node
        else:
            self.rear= new_node
            self.front=new_node
        

    def remove(self, index: int) -> bool:

        if(self.front is None):
            return False
        prev = self.front
        curr= self.front
        i=0
        while (curr!=None):
            if(i == index):
                # when first item and only item
                if(i==0 and self.front.next is  None):
                    self.front = None
                    self.rear =None
                    return True
                # when first item and list coniues 
                elif(i==0 and self.front.next is not  None) :
                    self.front = self.front.next
                    return True

                # last item then we update new rear
                elif(curr.next is None):
                    prev.next = curr.next
                    self.rear = prev
                    return True

                else: # for all other cases 
                    prev.next = curr.next
                    return True

            else:
                prev= curr
                curr=curr.next
                i+=1
        return False





















        

    def getValues(self) -> List[int]:
        curr = self.front
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
