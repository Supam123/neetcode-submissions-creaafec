class Node:
    def  __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [None] * capacity
        self.capacity =  capacity
        self.size = 0
    
    def hashFunc(self,key):
        return key % self.capacity
        
    def insert(self, key: int, value: int) -> None:
        index =  self.hashFunc(key)
        if(self.table[index]==None):
            newNode = Node(key,value)
            self.table[index]= newNode
        else:
            # linked list already exist | append to it
            curr =  self.table[index]
            prev = None
            while curr:
                if(curr.key == key):
                    curr.val =  value 
                    return
                prev =  curr
                curr = curr.next
            prev.next =  Node(key,value)
        self.size +=1
        if( (self.size / self.capacity) >= 0.5):
            self.resize()  
    
    def get(self, key: int) -> int:
        index =  self.hashFunc(key)
        curr =  self.table[index]
        while curr:
            if(curr.key == key):
                return curr.val
            curr= curr.next
        return -1


    def remove(self, key: int) -> bool:
        index =  self.hashFunc(key)
        node =  self.table[index]
        prev =  None
        while node:
            if(node.key==key):
                if(prev is None):
                    self.table[index] = node.next
                else:
                    prev.next=node.next               
                self.size -=1
                return True
            prev = node
            node= node.next
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newTable = [None] * newCapacity

        for node in self.table:
            while node:
                newIndex = node.key % newCapacity
                if(newTable[newIndex] is None):
                    newTable[newIndex] = Node(node.key,node.val)
                else:
                    curr =  newTable[newIndex]
                    while curr.next:
                        curr= curr.next
                    curr.next = Node(node.key,node.val)
                node =  node.next
        self.capacity =  newCapacity
        self.table =  newTable

                











