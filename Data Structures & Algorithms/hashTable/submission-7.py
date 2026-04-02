class Pair :
    def __init__(self,key,val):
        self.key= key
        self.value = val
        self.next = None
   
class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hashmap = [None] * capacity
 
    def hash_function(self,key):
        return key % self.capacity   

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.hashmap[index]
        
        if node is None:
            self.hashmap[index] = Pair(key,value)
            self.size+=1
        else:
            prev= None
            while node:
                if(node.key == key):
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = Pair(key,value)
            self.size +=1
        if( self.size / self.capacity>=0.5):
            self.resize()


   
   

    

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.hashmap[index]

        while node:
            if(node.key==key):
                return node.value
            node=node.next
        return -1
   



        
       
      
    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.hashmap[index]

        if node is None:
            return False
        else:
            prev= None
            while node:
                if node.key == key:
                    if prev is None:
                        self.hashmap[index] = node.next
                        self.size -=1
                        return True
                    else:
                        prev.next = node.next
                        self.size -=1
                        return True
                prev = node
                node=node.next
            return False
            
                 

    def getSize(self) -> int:
        return self.size
       


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        new_capacity = self.capacity *2
        new_map = [None]*new_capacity
        old_map = self.hashmap
        self.capacity = new_capacity
        for node in old_map:
            while node:
                next_node = node.next # u wanna store the next i the old chaning because u set node next in the new hashtable
                #that way we break the chaining link in the old so we perserve that
              
                index = node.key % self.capacity
                if(new_map[index] is None):
                    new_map[index] = Pair(node.key,node.value)
                else:
                    node.next = new_map[index]
                    new_map[index] = node
                   
                node =  next_node
        
        self.hashmap = new_map

      
        

      






