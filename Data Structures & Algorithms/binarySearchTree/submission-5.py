class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val) # create a new node first 
        if(self.root is None): # if the tree is empty then assign the root to newnode
            self.root = newNode
        curr = self.root
        while True:
            if(key>curr.key):
                if(curr.right is None):
                    curr.right = newNode
                    return
                curr = curr.right
            elif(key<curr.key):
                if(curr.left is None):
                    curr.left = newNode
                    return
                curr= curr.left
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:

        if(self.root is None):
            return -1
        
        curr = self.root
        while curr is not None:
            if(key<curr.key):
                curr = curr.left
            elif(key>curr.key):
                curr = curr.right
            else:
                return curr.val
        
        return -1


    def getMin(self) -> int:
        curr=self.root
        if(self.root is None):
            return -1
        while curr and curr.left is not None:
            curr = curr.left
        return curr.val


    def getMax(self) -> int:
        curr=self.root
        if(self.root is None):
            return -1
        while curr and curr.right is not None:
            curr = curr.right
        return curr.val
    
    def findMin(self,node):
        while node and node.left:
            node =  node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root,key)

    def removeHelper(self,root,key):
        if(root == None):
            return None
        if(key > root.key):
            root.right = self.removeHelper(root.right,key)
        elif(key < root.key):
            root.left =  self.removeHelper(root.left,key)
        else:
            if(root.left is None):
                return root.right
            elif(root.right is None):
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.key = minNode.key
                root.right  =self.removeHelper(root.right,minNode.key)
        return root






    def getInorderKeys(self) -> List[int]:

        result = []
        self.inorderTraversal(self.root,result)
        return result

    def inorderTraversal(self, root,result):
            if(root):
                self.inorderTraversal(root.left,result)
                result.append(root.key)
                self.inorderTraversal(root.right,result)















