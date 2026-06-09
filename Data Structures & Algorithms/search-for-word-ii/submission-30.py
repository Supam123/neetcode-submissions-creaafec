class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord =  False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr =  self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        mytree = Trie()
        for w in words:
            mytree.insert(w)
        visit = set()
        rows,cols = len(board),len(board[0])
        res = set()
        def dfs(r,c,curr,s):
            if r < 0 or c < 0 or r == rows or c==cols or (r,c) in visit or board[r][c] not in curr.children:
                return 

            visit.add((r,c))
            s += board[r][c]
            char = board[r][c]
            curr =  curr.children[char] # proceed forward
            if curr.endofWord: # if current is end of word append it
                res.add(s)

            dfs(r+1,c,curr,s) 
            dfs(r-1,c,curr,s) 
            dfs(r,c+1,curr,s) 
            dfs(r,c-1,curr,s)

            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,mytree.root,'')
        return list(res)
        

            















        