class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = {l:0 for word in words for l in word}
        # now we build the graph and indegree for our topo sort
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                word1 = words[i]
                word2 = words[j]
                minLen = min(len(word1),len(word2))
                if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                    return ''
                for k in range(minLen):
                    if word1[k] != word2[k]:
                        adj[word1[k]].append(word2[k])
                        indegree[word2[k]] += 1
                        break
        
        # pre seed the q with 0 indegrees
        q =  deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        res = ''
        while q:
            c = q.popleft()
            res += c
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == len(indegree) else ''






            
        