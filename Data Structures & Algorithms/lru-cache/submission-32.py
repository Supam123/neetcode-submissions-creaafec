class Node:
    def __init__(self,val=0,key=0):
        self.next  = None
        self.prev =  None
        self.val = val
        self.key =  key

class LRUCache:
    # in LRU the LRU is leftmost and MRU is rightmost

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev =  self.left
        self.cap = capacity
        self.cache = {}
    
    def remove(self,node):
        pre =  node.prev
        nxt =  node.next
        pre.next = nxt
        nxt.prev = pre
    
    def insert(self,node):
        last_node =  self.right.prev
        last_node.next = node
        node.prev = last_node
        node.next =  self.right
        self.right.prev =  node     
    
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node =  self.cache[key]
            self.remove(node)
        new_node =  Node(value,key)
        self.cache[key] = new_node # this maps the new node
        self.insert(new_node) # this inserts in DLL
        if len(self.cache) > self.cap:
            #then i have to delete the LRU leftmost node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            









        
