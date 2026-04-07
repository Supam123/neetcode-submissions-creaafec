class Node:
    def __init__(self,key = 0,val=0):
        self.val= val
        self.next = None
        self.key = key
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left =  Node(0)
        self.right = Node(0)
        self.left.next =  self.right

        self.right.prev = self.left
        self.cache = {}

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt 
        nxt.prev = prev
    
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  
            self.insert(self.cache[key])
            return self.cache[key].val
        return  -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.insert(new_node)
        if len(self.cache) > self.cap :
            # remove the LRU
            lru =  self.left.next
            self.remove(lru)
            del self.cache[lru.key]













        
