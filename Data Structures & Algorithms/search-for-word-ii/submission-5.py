class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class Tree:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTree = Tree()
        for word in words:
            myTree.insert(word)
        
        ROWS,COLS = len(board),len(board[0])
        res,visit = set(),set()
        
        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c) in visit) or board[r][c] not in node.children:
                return
            
            visit.add((r,c)) 
            ch = board[r][c]
            word += ch
            node = node.children[ch]
            if node.endofWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,myTree.root,'')
        

        return list(res)




       


















        