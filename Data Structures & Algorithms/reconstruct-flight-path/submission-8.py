class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        output = []
        # STEP 1 BUILD AN ADJ LIST so we know where to travel from and to what
        adj = defaultdict(list)
        tickets = sorted(tickets)
        for src,dst in tickets:
            adj[src].append(dst)
        output.append('JFK')


        def dfs(airport):
            if len(output) == len(tickets) + 1:
                return True # then we have travelled everywhere
            if src not in adj:
                return False
         
            for i in range(len(adj[airport])): # all the desitnations from JFK
                nei_airport = adj[airport][i]
                adj[airport].pop(i)
                output.append(nei_airport)

                if dfs(nei_airport) == True:
                    return True

                adj[airport].insert(i,nei_airport)
                output.pop() # we remove the last choice 
                # then we automatiaclly loop the enxt choice 
                #  JFK = [HKL false emptty stuck,JUI s,LOP,DVC,LOW]
                '''
                DFS JFK
                  |
                  V
                DFS HKL
                  |
                  V
                we never return true from base case adn foor loop is empty so it just nifhses 
                and never returns true hence then we isnert it back to trickert snad remove from path
                and then we try the next nei of jfk that mifht lead us to fuckign answer                  
                '''
            return False # we return false if there are no nei menains we stuck so we back track adn try another choice.

        dfs('JFK')
        return output
            

            
      
