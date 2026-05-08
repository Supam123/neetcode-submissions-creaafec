from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjL = defaultdict(list)
        # two words are neighbors if they differ in one char
        # two words are neigbors if they share the same pattern 
        # which would mean that its same word can be made at the wildcard
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adjL[pattern].append(word)
                #IMPORTANT TWO WORDS THAT SHARE THE SAME PATTERN ARE NEOIGBORS 
        q = deque()
        visit =set()
        q.append(beginWord)
        visit.add(beginWord)
        steps = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                # then add its neigbirs 
                # get its pattern and see what words ahre this apttern hence they are neiogbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjL[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            steps +=1
        return 0
                    


        