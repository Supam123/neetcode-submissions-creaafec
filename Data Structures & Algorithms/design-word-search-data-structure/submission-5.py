class TrieNode:
    def __init__(self):
        self.child = {}
        self.endofWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr =  curr.child[w]
        curr.endofWord = True

        

    def search(self, word: str) -> bool:

        def dfs(node,index):
            if index == len(word):
                return node.endofWord
            
            ch = word[index]
            if ch != '.':
                if ch not in node.child:
                    return False
                return dfs(node.child[ch], index+1)
            else:
                for c in node.child:
                    if dfs(node.child[c],index+1):
                        return True
                return False
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)