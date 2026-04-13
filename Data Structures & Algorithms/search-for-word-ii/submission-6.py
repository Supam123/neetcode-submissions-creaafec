class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]  = TrieNode()
            curr = curr.children[w]
        curr.endofWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = Trie()
        for word in words:
            myTrie.insert(word)



        ROWS,COLS = len(board),len(board[0])
        visit = set()
        output = set()
        def dfs(r,c,node,word):
            nonlocal output
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endofWord:
                output.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,myTrie.root,'')
        return list(output)







       






















        