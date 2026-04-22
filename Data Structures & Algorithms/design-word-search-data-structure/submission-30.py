class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        curr =  self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr =  curr.children[w]
        curr.endofWord = True       

    def search(self, word: str) -> bool:
        
        def dfs(i,root):
            if i == len(word):
                return root.endofWord
            
            ch = word[i]
            if ch != '.':
                if ch not in root.children:
                    return False
                return dfs(i+1, root.children[ch])
            else:
                for c in root.children:
                    if dfs(i+1,root.children[c]):
                        return True
                return False
        



        return dfs(0,self.root)















        
