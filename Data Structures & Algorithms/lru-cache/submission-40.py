class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev=None
        self.next= None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache={}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        #
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self,node):
        #
        prev = self.right.prev
        self.right.prev = node
        node.next =  self.right
        prev.next = node
        node.prev = prev

        
    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # since its used to get this is the most recently used we swap
        return -1
             

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # remove the duplicate and insert the new key:val pair
        self.cache[key]= Node(key,val)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap :
            #then we remove the LRU
            left = self.left.next
            del self.cache[left.key]
            self.remove(left)
      


        
