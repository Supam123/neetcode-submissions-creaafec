class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj =  defaultdict(list)
        indegree = {l:0 for word in words for l in word}
        # now we are going to construct graph i.e. adj and indegree
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen =  min(len(word1),len(word2))
            if len(word1)>len(word2) and word1[:minLen] == word2[:minLen]:
                return ''
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        res = ''
        while q:
            node =  q.popleft()
            res += node
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == len(indegree) else ''




       
        