class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}
        # n = len(cost)

        # def dfs(i):
        #     if i <= 1:
        #         return cost[i]
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = cost[i] + min(dfs(i-1),dfs(i-2))
        #     return memo[i]
        # return min(dfs(n-1),dfs(n-2))
        n = len(cost)
        twoStepBackCost = cost[0]
        oneStepBackCost = cost[1]
        for i in range(2,n):
            curr_cost = cost[i] + min(twoStepBackCost , oneStepBackCost)
            twoStepBackCost = oneStepBackCost
            oneStepBackCost = curr_cost
        return min(oneStepBackCost,twoStepBackCost)


      
            
        