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
            curr = curr.children[w]
        curr.endofWord = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.endofWord #  meaning we checked all the indexes
            ch = word[i]
            # now ch can be two things a dot and actual char
            if ch != '.':
                if ch not in node.children:
                    return False # ch just dont exist to be searched upon
                else:
                    return dfs(node.children[ch],i+1)
            else:
                # then we try all the possible macthes of the node
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
        return dfs(self.root,0)
       







        
