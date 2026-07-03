class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)# we use set cuz we might have duplcaite edges
        indegree = {l : 0 for word in words for l in word}
    
        # now we build the graph
        for i in range(len(words)-1):
            word1 = words[i]
            word2 =  words[i+1]
            minLen = min(len(word1),len(word2)) # abc ab
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ''
            # now who do i loop thru
            for j in range(minLen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        result = ''
        while q:
            letter = q.popleft()
            result += letter
            # all the other ketter that i can unlock after this
            for nei in adj[letter]:
                indegree[nei] -= 1
                if indegree[nei] ==0:
                    q.append(nei)
        return result if len(result) == len(indegree) else ''


      
      