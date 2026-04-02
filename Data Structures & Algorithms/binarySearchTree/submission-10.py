class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)
        if(self.root is None) : # i.e. this is the first node to be inserted
            self.root =  newNode
            return
        curr =  self.root
        while curr:
            if(key < curr.key):
                if(curr.left is None):
                    curr.left = newNode
                curr = curr.left
            elif(key > curr.key):
                if(curr.right is None):
                    curr.right = newNode
                curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:

        curr = self.root
        while curr:
            if(key < curr.key):
                curr = curr.left
            elif(key> curr.key):
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.root
        while curr:
            if(curr.left is None):
                return curr.val
            curr = curr.left
        return  -1



    def getMax(self) -> int:
        curr = self.root
        while curr:
            if(curr.right is None):
                return curr.val
            curr = curr.right
        return -1

    def findMin(self,node):
        while node:
            if(node.left is None):
                return node
            node=node.left
        

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root,key)

    def removeHelper(self,curr,key):

        if(curr is None):
            return None
        
        if(key < curr.key):
            curr.left = self.removeHelper(curr.left,key)
        elif(key > curr.key):
            curr.right = self.removeHelper(curr.right,key)
        else:
            # that means we have reached the value we want to remove
            if(curr.left is None):
                return curr.right
            elif(curr.right is None):
                return curr.left
            else:
                minNode =  self.findMin(curr.right)
                curr.val = minNode.val
                curr.key = minNode.key
                curr.right = self.removeHelper(curr.right,minNode.key)
        return curr













    def getInorderKeys(self) -> List[int]:
        res =  []
        def inOrder(root):
            if(root is None):
                return
            inOrder(root.left)
            res.append(root.key)
            inOrder(root.right)
        
        inOrder(self.root)
        return res

