class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr =  self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofWord =  True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTree = Trie()
        for word in words:
            myTree.insert(word)
        
        ROWS,COLS =  len(board),len(board[0])
        visited = set()
        result = set()
        def dfs(r,c,root,word):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited or board[r][c] not in root.children:
                return
            visited.add((r,c))
            word += board[r][c]
            root = root.children[board[r][c]]
            
            if root.endofWord:
                result.add(word)
            dfs(r+1,c,root,word)
            dfs(r-1,c,root,word)
            dfs(r,c+1,root,word)
            dfs(r,c-1,root,word)

            #backtracking
            visited.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,myTree.root,'')
        return list(result)














        