class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofWord =  True

    def search(self, word: str) -> bool:
        
        def dfs(curr,i):
            if i == len(word):
                return curr.endofWord
            
            ch = word[i]
            if ch != '.':
                if ch in curr.children:
                    return dfs(curr.children[ch],i+1)
                else:
                    return False
            else:
                for c in curr.children.values():
                    if dfs(c,i+1):
                        return True
                return False
        return dfs(self.root,0)












        
