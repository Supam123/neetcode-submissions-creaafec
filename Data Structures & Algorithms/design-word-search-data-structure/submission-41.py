class TrieNode:
    def  __init__(self):
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
        curr.endofWord =  True       

    def search(self, word: str) -> bool:
        i = 0
        def dfs(i,node):
            if i == len(word):
                return node.endofWord
            ch = word[i]
            if ch != '.' and ch not in node.children:
                return False
            if ch == '.':
                for c in node.children:
                    if  dfs(i+1,node.children[c]) == True:
                        return True
                return False
            else:
                if dfs(i+1,node.children[ch]) == False:
                    return False
                else:
                    return True
        return dfs(0,self.root)
        










        
