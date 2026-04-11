class Node:
    def __init__(self,val=0,key = 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
    
    def insert(self,node):
        last_node = self.right.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.right
        self.right.prev = node


        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node =  Node(value,key)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            #remove the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]






        
