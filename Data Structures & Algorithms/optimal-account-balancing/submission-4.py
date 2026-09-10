class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        nodes = defaultdict(int)
        for f,t,a in transactions:
            nodes[f] -= a
            nodes[t] += a
        '''
        0 = -5, 1= +10, 2= -5
        '''
        postives = [v for v in nodes.values() if v>0]
        negatives = [v for v in nodes.values() if v<0]

        def dfs(pos,neg):
            if not pos or not neg : return 0

            p = pos[0]
            mini = float('inf')

            for j in range(len(neg)):
                n = neg[j]

                if p == -n:
                    r_pos = pos[1:]
                    r_neg = neg[0:j] + neg[j+1:]
                    return 1 + dfs(r_pos,r_neg)
                elif p < -n:
                    r_pos = pos[1:]
                    r_neg = neg[0:j] + [n+p] + neg[j+1:]
                    mini =  min(mini,1+dfs(r_pos,r_neg))
                else:
                    r_pos = [n+p] + pos[1:]
                    r_neg = neg[0:j] + neg[j+1:]
                    mini =  min(mini,1+dfs(r_pos,r_neg))
            return mini
        return dfs(postives,negatives)










       
        