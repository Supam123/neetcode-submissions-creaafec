class Node:
    def __init__(self,key=0,val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.hashmap = {}
        self.cap = capacity
        
        

    def insert(self,new_node):
        prevN = self.right.prev
        prevN.next = new_node
        new_node.prev = prevN
        new_node.next = self.right
        self.right.prev = new_node
      
    
    def remove(self,node):
        prevN =  node.prev
        nxtN = node.next
        prevN.next = nxtN
        nxtN.prev = prevN
       
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            new_node = Node(key,value)
            self.insert(new_node)
            self.hashmap[key] = new_node

        else:
            new_node = Node(key,value)
            self.hashmap[key] = new_node
            self.insert(new_node)
            if len(self.hashmap) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.hashmap[lru.key]







        
