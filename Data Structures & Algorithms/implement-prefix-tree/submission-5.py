class TrieNode:

    def __init__(self):
        self.children = {}
        self.endofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # word  = cat
        curr =  self.root 
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w in curr.children:
                curr = curr.children[w]
            else:
                return False
        return curr.endofWord

        

    def startsWith(self, prefix: str) -> bool:
        curr =  self.root
        for w in prefix:
            if w in curr.children:
                curr = curr.children[w]
            else:
                return False
        return True










        
        