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
                curr.children[w] =TrieNode()
            curr = curr.children[w]
        curr.endofWord = True
    def search(self, word: str) -> bool:

        def dfs(node,index):

            if index == len(word):
                return node.endofWord
            ch = word[index]
            if ch != '.':
                if ch not in node.children:
                    return False
                else:
                    return dfs(node.children[ch],index+1)
            else:
                for c in node.children.values():
                    if dfs(c,index+1):
                        return True
                return False
        return dfs(self.root,0)