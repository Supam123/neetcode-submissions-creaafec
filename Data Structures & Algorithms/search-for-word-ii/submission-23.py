class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class Trie:
    def __init__(self):
        self.root =  TrieNode()
    def insert(self,word):
        curr =  self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTree = Trie()
        for w in words:
            myTree.insert(w)
        
        ROWS,COLS =  len(board),len(board[0])
        visit = set()
        res = set()
        def dfs(r,c,root,curr_word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in root.children:
                return
            visit.add((r,c))
            curr_word += board[r][c]
            ch = board[r][c]
            root = root.children[ch]
            if root.endofWord:
                res.add(curr_word)
            
            dfs(r+1,c,root,curr_word)
            dfs(r-1,c,root,curr_word)
            dfs(r,c+1,root,curr_word)
            dfs(r,c-1,root,curr_word)

            visit.remove((r,c))         
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,myTree.root,'')
        return list(res)















        