class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class WordDictionary:

    def __init__(self):
        self.root =  TrieNode()
        

    def addWord(self, word: str) -> None:
        curr =  self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr =  curr.children[w]
        curr.endofWord = True        

    def search(self, word: str) -> bool:

      
        def dfs(root,index):
            if index == len(word):
                return root.endofWord
            ch = word[index]
            if ch != '.':
                if ch not in root.children:
                    return False
                else:
                    return dfs(root.children[ch],index+1)
            else:
                for c in root.children.values():
                    if dfs(c,index+1):
                        return True
                return False
        return dfs(self.root,0)
            











        
